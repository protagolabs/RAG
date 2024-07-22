from src.chunk import process_folder
from src.summary import process_summarize, process_summarize_entity
from src.extract_entity import save_entity
from src.entity_resolution import entities_and_relationships_resolution
from src.hierarchical_leiden_cluster import process_and_cluster_entities
from src.query2entity import process_query_to_entity

if __name__ == "__main__":

    # Chunk docs
    folder_path = 'input/harryPotter'  # Replace with the path to your folder
    raw_file = 'jsonl/raw.jsonl'

    #chunks = process_folder(folder_path,raw_file)

    #print(f"Processed {len(chunks)} chunks and wrote to {raw_file}")

    # summarize chunks
    raw_summary_file = 'jsonl/raw_summary.jsonl'
    #process_summarize(raw_file,raw_summary_file)
    
    # extract entity
    raw_entity_file = 'jsonl/raw_entity.jsonl'  
    #save_entity(raw_summary_file, raw_entity_file)

    # entity resolution
    resolution_file = 'jsonl/resolution.jsonl'
    #entities_and_relationships_resolution(raw_entity_file, resolution_file)

    # summarize entity
    entity_input_file = 'jsonl/resolution_entities.jsonl'
    entity_summary_file = 'jsonl/resolution_entity_summary.jsonl'
    #process_summarize_entity(entity_input_file, entity_summary_file)

    # hierarchical leiden clustering
    relation_input_file = 'jsonl/resolution_relationships.jsonl'
    cluster_file = 'jsonl/community_report.jsonl'
    #process_and_cluster_entities(entity_summary_file, relation_input_file, cluster_file, max_cluster_size=10)

    # query to entity
    output_file = 'jsonl/query_to_entity.jsonl'
    #Query = 'Who are the friend of Harry Potter?'
    Query = 'Who is the stongest person?'
    process_query_to_entity(Query, output_file)

    # findout doc_id based on query and filter them based on query

