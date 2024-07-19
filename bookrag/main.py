from src.chunk import process_folder
from src.summary import process_summarize
from src.extract_entity import save_entity
from src.entity_resolution import entities_and_relationships_resolution

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