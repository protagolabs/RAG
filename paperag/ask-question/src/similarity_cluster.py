import json
import numpy as np
import jsonlines
import ollama
import igraph as ig
import leidenalg as la
from sklearn.metrics.pairwise import cosine_similarity

# filter raw answers
def filter_answer(input_file, output_file, score_threshold=80):
    # Read JSONL file using jsonlines
    with jsonlines.open(input_file, mode='r') as reader:
        data = [doc for doc in reader]

    # Collect all points globally
    all_points = []
    for entry in data:
        for point in entry['points']:
            if point['score'] >= score_threshold:
                all_points.append({"doc_id": entry['doc_id'], "description": point['description'], "score": point['score']})

    # Sort the points globally based on score
    all_points.sort(key=lambda x: x['score'], reverse=True)

    # Write the processed data to a new JSONL file using jsonlines
    with jsonlines.open(output_file, mode='w') as writer:
        for entry in all_points:
            writer.write(entry)

    print(f"Filtered and globally ranked data saved to {output_file}")

    return all_points

# Function to calculate embedding for each point
def calculate_embedding(point):
    embedding = ollama.embeddings(model='mxbai-embed-large', prompt=point)["embedding"]
    return embedding

# clustering answers
def leiden_cluster_points(points, output_file, resolution_parameter=1.4):

    # Calculate embeddings for all points
    embeddings = np.array([calculate_embedding(point) for point in points])

    # Construct similarity graph using cosine similarity
    similarity_matrix = cosine_similarity(embeddings)
    np.fill_diagonal(similarity_matrix, 0)  # Remove self-similarity
    edges = np.argwhere(similarity_matrix > 0)
    weights = similarity_matrix[edges[:, 0], edges[:, 1]]

    # Create igraph graph
    g = ig.Graph()
    g.add_vertices(len(points))
    g.add_edges(edges)
    g.es['weight'] = weights

    # Apply Leiden Algorithm
    partition = la.find_partition(g, la.CPMVertexPartition, weights='weight', resolution_parameter=resolution_parameter)

    # Organize points by cluster labels
    clusters = {}
    for idx, cluster_id in enumerate(partition.membership):
        if cluster_id not in clusters:
            clusters[cluster_id] = []
        clusters[cluster_id].append(points[idx])

    # Save clusters to a JSONL file
    with jsonlines.open(output_file, mode='w') as writer:
        for label, points in clusters.items():
            writer.write({str(label): points})

    print(f"Clusters saved to {output_file}")


if __name__ == "__main__":

    # filter raw answers
    input_file = 'jsonl/raw_answers.jsonl'
    output_file = 'jsonl/filter_answers.jsonl'
    all_points = filter_answer(input_file, output_file)

    # clustering
    # Sample list of points
    points = [all_point["description"] for all_point in all_points] 
    output_file = 'jsonl/cluster_points.jsonl'
    leiden_cluster_points(points, output_file)


