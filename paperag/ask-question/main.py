from src.qa import map_reduce_documents
from src.similarity_cluster import filter_answer
from src.extract_entity import save_entity
from src.entity_resolution import entities_and_relationships_resolution
from src.hierarchical_leiden_cluster import process_and_cluster_entities
from src.aggregate import process_aggregate

if __name__ == "__main__":
    # generate raw answers
    input_file = '../chunk/output.jsonl'
    raw_answers_file = 'jsonl/raw_answers.jsonl'  
    question = "When integrating the autonomous vehicle into urban cities, what are the challenges and what are the opportunities? If you only know one, please provide the one you know. You can also provide both if you know both."  

    #map_reduce_documents(input_file, raw_answers_file, question)

    # filter raw answers
    filter_answer_file = 'jsonl/filter_answers.jsonl'
    #filter_answer = filter_answer(raw_answers_file, filter_answer_file)

    # extract entities
    raw_entity_file = 'jsonl/raw_entity.jsonl'
    #save_entity(filter_answer_file, raw_entity_file)

    # entity resolusion
    resolution_file = 'jsonl/resolution.jsonl'
    entities_and_relationships_resolution(raw_entity_file, resolution_file)

    # cluster entities
    entity_file = 'jsonl/resolution_entities.jsonl'
    relation_file = 'jsonl/resolution_relationships.jsonl'
    # save the cluster output
    cluster_file = 'jsonl/hierarchical_cluster_result.jsonl'

    process_and_cluster_entities(entity_file, relation_file, cluster_file)

    # aggregate the cluster output
    output_file = 'jsonl/output.jsonl'  # Replace with your desired output file path
    process_aggregate(cluster_file, output_file, question)