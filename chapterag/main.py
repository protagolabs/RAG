from src.chunk import process_folder
from src.summary import process_summarize
from src.qa import map_reduce_documents
from src.aggregate import process_aggregate

if __name__ == "__main__":

    # Chunk docs
    folder_path = 'input/smartCity'  # Replace with the path to your folder
    raw_file = 'jsonl/raw.jsonl'

    #chunks = process_folder(folder_path,raw_file)

    #print(f"Processed {len(chunks)} chunks and wrote to {raw_file}")

    # summarize chunks
    raw_summary_file = 'jsonl/raw_summary.jsonl'
    #process_summarize(raw_file,raw_summary_file)
    

    # direct qa
    output_qa_file = 'jsonl/raw_answers.jsonl' 
    question = "what are the urban mobility challenge nowadays? when you answerm it is better to give reasons or examples."
    #map_reduce_documents(raw_summary_file, output_qa_file, question)


    # aggregate
    output_file= 'jsonl/answer.jsonl'
    process_aggregate(output_qa_file, output_file, question)