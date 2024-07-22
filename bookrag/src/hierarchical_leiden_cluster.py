import networkx as nx
import igraph as ig
from .summary import summarize_report
import jsonlines
import json
from graspologic.utils import largest_connected_component
from collections import defaultdict
from typing import Any, cast, Optional, List, Dict
import logging
import re
import pickle
import torch
import ollama
from openai import OpenAI
from graspologic.partition import hierarchical_leiden
from .milvus_database import initialize_and_insert_data
log = logging.getLogger(__name__)

# Initialize the LLM client
client = OpenAI(
    base_url='http://localhost:11434/v1',
    api_key='gemma2'
)

# Function to calculate embedding for each point
def calculate_embedding(point):
    embedding = ollama.embeddings(model='mxbai-embed-large', prompt=point)["embedding"]
    return embedding

def extract_dict_from_json(text: str):
        """
        Extract the dictionary between "```json" and "```". 
        """
        pattern = r'```json(.*?)```'
        extracted_text = re.findall(pattern, text, re.DOTALL)

        return extracted_text[0].strip() 

def stable_largest_connected_component(graph: nx.Graph) -> nx.Graph:
    """Return the largest connected component of the graph, with nodes and edges sorted in a stable way."""
    graph = graph.copy()
    graph = cast(nx.Graph, largest_connected_component(graph))

    return _stabilize_graph(graph)

def _stabilize_graph(graph: nx.Graph) -> nx.Graph:
    """Ensure an undirected graph with the same relationships will always be read the same way."""
    fixed_graph = nx.DiGraph() if graph.is_directed() else nx.Graph()

    sorted_nodes = graph.nodes(data=True)
    sorted_nodes = sorted(sorted_nodes, key=lambda x: x[0])

    fixed_graph.add_nodes_from(sorted_nodes)
    edges = list(graph.edges(data=True))

    # If the graph is undirected, we create the edges in a stable way, so we get the same results
    # for example:
    # A -> B
    # in graph theory is the same as
    # B -> A
    # in an undirected graph
    # however, this can lead to downstream issues because sometimes
    # consumers read graph.nodes() which ends up being [A, B] and sometimes it's [B, A]
    # but they base some of their logic on the order of the nodes, so the order ends up being important
    # so we sort the nodes in the edge in a stable way, so that we always get the same order
    if not graph.is_directed():

        def _sort_source_target(edge):
            source, target, edge_data = edge
            if source > target:
                temp = source
                source = target
                target = temp
            return source, target, edge_data

        edges = [_sort_source_target(edge) for edge in edges]

    def _get_edge_key(source: Any, target: Any) -> str:
        return f"{source} -> {target}"

    edges = sorted(edges, key=lambda x: _get_edge_key(x[0], x[1]))

    fixed_graph.add_edges_from(edges)
    return fixed_graph

def _run(graph: nx.Graph, max_cluster_size: int, levels: Optional[List[int]], seed=42) -> Dict[int, Dict[str, List[str]]]:
    """Run method definition."""    

    
    log.info("Running leiden with max_cluster_size=%s, lcc=%s", max_cluster_size)

    node_id_to_community_map = _compute_leiden_communities(
        graph=graph,
        max_cluster_size=max_cluster_size,
        seed=seed,
    )

    # If they don't pass in levels, use them all
    if levels is None:
        levels = sorted(node_id_to_community_map.keys())

    results_by_level: Dict[int, Dict[str, List[str]]] = {}
    for level in levels:
        result = {}
        results_by_level[level] = result
        for node_id, raw_community_id in node_id_to_community_map[level].items():
            community_id = str(raw_community_id)
            if community_id not in result:
                result[community_id] = []
            result[community_id].append(node_id)
    return results_by_level

def _compute_leiden_communities(
    graph: nx.Graph,
    max_cluster_size: int,
    seed: int,
) -> Dict[int, Dict[str, int]]:
    """Return Leiden root communities."""
    graph = stable_largest_connected_component(graph)

    community_mapping = hierarchical_leiden(
        graph, max_cluster_size=max_cluster_size, random_seed=seed
    )
    results: Dict[int, Dict[str, int]] = {}
    for partition in community_mapping:
        results[partition.level] = results.get(partition.level, {})
        results[partition.level][partition.node] = partition.cluster

    return results

# def print_clusters_with_text(graph, clustering_result):
#     for level in sorted(clustering_result.keys()):
#         print(f"\nLevel {level}:")
#         communities = clustering_result[level]

#         for community_id, nodes in communities.items():
#             print(f"\nCommunity {community_id}:")
#             unique = set()
#             for node in nodes:
#                 if graph.nodes[node]['original_text'] not in unique:
#                     unique.add(graph.nodes[node]['original_text'])
#                     print(f"Node: {node}, Original Text: {graph.nodes[node]['original_text']}")
#                 else:
#                     print(f"Node: {node}")

# def save_clusters_to_jsonl(graph, clustering_result, output_file):
#     with jsonlines.open(output_file, mode='w') as writer:
#         for level in sorted(clustering_result.keys()):
#             communities = clustering_result[level]
#             for community_id, nodes in communities.items():
#                 key = f"level_{level}_community_{community_id}"
#                 unique_texts = {graph.nodes[node]['description'] for node in nodes}
#                 value = list(unique_texts)
#                 writer.write({key: value})

def get_communities_and_relationships(graph, communities_by_level,output_file):

    # Read existing keys from the output file
    existing_communities = set()
    try:
        with jsonlines.open(output_file) as reader:
            for obj in reader:
                for key in obj:
                    if key != 'doc_id':
                        existing_communities.add(key)
    except FileNotFoundError:
        pass

    community_details = defaultdict(lambda: {'nodes': [], 'edges': []})
    doc_details = defaultdict(list)
    with jsonlines.open(output_file, mode='a') as writer:
        # For each level, extract nodes and edges
        for level, communities in communities_by_level.items():
            for community_id, nodes in communities.items():
                key = f"level_{level}_community_{community_id}"
                # Skip if the community is already processed
                if key in existing_communities:
                    continue
                if len(nodes) == 0:
                    continue
                # Add nodes to the community with details
                for node in nodes:
                    node_details = {
                        'name': node,
                        'type': graph.nodes[node]['type'],
                        'description': graph.nodes[node]['description'],
                    }
                    community_details[community_id]['nodes'].append(node_details)
                    doc_details[community_id] += graph.nodes[node]['doc_id']
                
                # Find all edges within this community
                for node in nodes:
                    for neighbor in graph.neighbors(node):
                        if neighbor in nodes:  # Only consider edges within the community
                            edge = tuple(sorted((node, neighbor)))
                            if edge not in community_details[community_id]['edges']:
                                edge_details = {
                                    'source': node,
                                    'target': neighbor,
                                    'description': graph[node][neighbor]['description']
                                }
                                community_details[community_id]['edges'].append(edge_details)
                
                # generate report for this community
                community_report = summarize_report(str(community_details[community_id]))
                community_report = extract_dict_from_json(community_report)
                try:
                    community_report = json.loads(community_report)
                except:
                    community_report = community_report
                
                writer.write({key: community_report, 'doc_id': doc_details[community_id]})

    #return community_details

def process_and_cluster_entities(entity_file, relation_file, output_file, max_cluster_size=10):
    # Read entities from input_file1
    with jsonlines.open(entity_file, mode='r') as reader:
        entities = [doc for doc in reader]

    # Read relationships from input_file2
    with jsonlines.open(relation_file, mode='r') as reader:
        relationships = [doc for doc in reader]

    # Create a set of valid entity names
    valid_entity_names = {entity['name'] for entity in entities}

    # Filter relationships
    filtered_relationships = [
        relationship for relationship in relationships
        if relationship['source'] in valid_entity_names and relationship['target'] in valid_entity_names
    ]

    # save embeddings of entity and relationship to milvus

    entity_collection_name = "graphrag_entity_collection"
    relationship_collection_name = "graphrag_relationship_collection"
    entity_embeddings = [(entity['name'], entity['type'], entity['entity_descritpion_summary'], calculate_embedding(entity['name'])) for entity in entities]
    relationship_embeddings = [(relationship['source'], relationship['target'], relationship['description'], calculate_embedding(relationship['description'])) for relationship in filtered_relationships]
    initialize_and_insert_data(entity_collection_name, relationship_collection_name, entity_embeddings, relationship_embeddings)
    
    # merge relationships
    # Initialize a dictionary to hold the merged data
    merged_relationship = {}

    for item in filtered_relationships:
        key = (item['source'], item['target'])
        if key not in merged_relationship:
            merged_relationship[key] = {
                'doc_id': {item['doc_id']},
                'filename': {item['filename']},
                'description': [item['description']],
                'strength': item['strength']
            }
        else:
            merged_relationship[key]['doc_id'].add(item['doc_id'])
            merged_relationship[key]['filename'].add(item['filename'])
            merged_relationship[key]['description'].append(item['description'])
            merged_relationship[key]['strength'] += item['strength']

    # Convert merged_data dictionary back to a list
    final_relationships = []
    for (source, target), values in merged_relationship.items():
        final_relationships.append({
            'source': source,
            'target': target,
            'doc_id': list(values['doc_id']),
            'filename': list(values['filename']),
            'description': values['description'],
            'strength': values['strength']
        })

    # Create a networkx graph
    G = nx.Graph()

    # Add entities as nodes
    for entity in entities:
        G.add_node(entity['name'], type=entity['type'], description=entity['entity_descritpion_summary'], doc_id=list(set(entity['doc_id'])))

    # Add relationships as edges with float weights
    for relationship in final_relationships:
        #G.add_edge(relationship['source'], relationship['target'], description=relationship['description'], weight=float(relationship['strength']))
        #G.add_edge(relationship['source'], relationship['target'], weight=float(1))
        G.add_edge(relationship['source'], relationship['target'], description=relationship['description'], weight=float(len(relationship['description'])))

    # Run the clustering
    clustering_result = _run(G, max_cluster_size, None)

    # Save the clusters with original text to JSONL
    #save_clusters_to_jsonl(G, clustering_result, output_file)
    # Collect community details
    get_communities_and_relationships(G, clustering_result, output_file)
    
    
    # Save the graph to a file
    with open('jsonl/graph.pkl', 'wb') as f:
        pickle.dump(G, f)
    

if __name__ == "__main__":
    
    entity_file = 'jsonl/resolution_entities.jsonl'
    relation_file = 'jsonl/resolution_relationships.jsonl'
    # Define the output file
    output_file = 'jsonl/hierarchical_cluster_result.jsonl'

    process_and_cluster_entities(entity_file, relation_file, output_file)