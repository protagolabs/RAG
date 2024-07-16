import json
import numpy as np
import jsonlines
import ollama
import igraph as ig
import leidenalg as la
from sklearn.metrics.pairwise import cosine_similarity

# Function to read a JSONL file
def read_jsonl(file_path):
    data = []
    with open(file_path, 'r') as file:
        for line in file:
            data.append(json.loads(line.strip()))
    return data

# Function to write to a JSONL file
def write_jsonl(file_path, data):
    with open(file_path, 'w') as file:
        for entry in data:
            file.write(json.dumps(entry) + "\n")

# Load the data from the input JSONL file
input_file = 'output_answers.jsonl'
data = read_jsonl(input_file)

# Collect all points globally
all_points = []
for entry in data:
    for point in entry['points']:
        if point['score'] >= 80:
            all_points.append({"doc_id": entry['doc_id'], "description": point['description'], "score": point['score']})


# Function to calculate embedding for each point
def calculate_embedding(point):
    embedding = ollama.embeddings(model='mxbai-embed-large', prompt=point)["embedding"]
    return embedding

# Sample list of points
points = [all_point["description"] for all_point in all_points]  

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
partition = la.find_partition(g, la.CPMVertexPartition, weights='weight', resolution_parameter=1.2)


# Organize points by cluster labels
clusters = {}
for idx, cluster_id in enumerate(partition.membership):
    if cluster_id not in clusters:
        clusters[cluster_id] = []
    clusters[cluster_id].append(points[idx])

# Save clusters to a JSONL file
with jsonlines.open('clustered_points.jsonl', mode='w') as writer:
    for label, points in clusters.items():
        writer.write({str(label): points})

print("Clusters saved to clustered_points.jsonl")


# Sort the points globally based on score
all_points.sort(key=lambda x: x['score'], reverse=True)
# Write the processed data to a new JSONL file
output_file = 'filtered_ranked_global_data.jsonl'
write_jsonl(output_file, all_points)

print(f"Filtered and globally ranked data saved to {output_file}")
