import networkx as nx
import igraph as ig
import matplotlib.pyplot as plt
import jsonlines
from graspologic.utils import largest_connected_component
from typing import Any, cast, Optional, List, Dict
import logging
from graspologic.partition import hierarchical_leiden
log = logging.getLogger(__name__)

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
    use_lcc = True
    

    
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

def print_clusters_with_text(graph, clustering_result):
    for level in sorted(clustering_result.keys()):
        print(f"\nLevel {level}:")
        communities = clustering_result[level]

        for community_id, nodes in communities.items():
            print(f"\nCommunity {community_id}:")
            unique = set()
            for node in nodes:
                if graph.nodes[node]['original_text'] not in unique:
                    unique.add(graph.nodes[node]['original_text'])
                    print(f"Node: {node}, Original Text: {graph.nodes[node]['original_text']}")
                else:
                    print(f"Node: {node}")

def save_clusters_to_jsonl(graph, clustering_result, output_file):
    with jsonlines.open(output_file, mode='w') as writer:
        for level in sorted(clustering_result.keys()):
            communities = clustering_result[level]
            for community_id, nodes in communities.items():
                key = f"level_{level}_community_{community_id}"
                unique_texts = {graph.nodes[node]['original_text'] for node in nodes}
                value = list(unique_texts)
                writer.write({key: value})

def process_and_cluster_entities(entity_file, relation_file, output_file, max_cluster_size=20):
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

    # Create a networkx graph
    G = nx.Graph()

    # Add entities as nodes
    for entity in entities:
        G.add_node(entity['name'], type=entity['type'], description=entity['description'], original_text=entity['original_text'])

    # Add relationships as edges with float weights
    for relationship in filtered_relationships:
        #G.add_edge(relationship['source'], relationship['target'], weight=float(relationship['strength']))
        G.add_edge(relationship['source'], relationship['target'], weight=float(1))

    # Run the clustering
    clustering_result = _run(G, max_cluster_size, None)

    # Save the clusters with original text to JSONL
    save_clusters_to_jsonl(G, clustering_result, output_file)

if __name__ == "__main__":
    
    entity_file = 'jsonl/resolution_entities.jsonl'
    relation_file = 'jsonl/resolution_relationships.jsonl'
    # Define the output file
    output_file = 'jsonl/hierarchical_cluster_result.jsonl'

    process_and_cluster_entities(entity_file, relation_file, output_file)