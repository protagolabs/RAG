import os
import json
import jsonlines
import tiktoken
import re


def chunk_text_by_paragraph(text, min_tokens=500, max_tokens=1000, encoding_name='cl100k_base'):
    """
    Chunk text by tokens.

    :param text: The input text to chunk.
    :param min_tokens: Minimum number of tokens per chunk.
    :param max_tokens: Maximum number of tokens per chunk.
    :param encoding_name: Encoding name for the tokenizer.
    :return: List of text chunks.
    """
    enc = tiktoken.get_encoding(encoding_name)
    paragraphs = text.split('\n\n')
    chunks = []
    current_chunk = []
    current_tokens = 0

    for paragraph in paragraphs:
        if not is_valid_sentence(paragraph):
            continue
        paragraph_tokens = len(enc.encode(paragraph))
        
        if current_tokens + paragraph_tokens > max_tokens:
            if current_tokens >= min_tokens:
                chunks.append('\n\n'.join(current_chunk))
                current_chunk = [paragraph]
                current_tokens = paragraph_tokens
            else:
                current_chunk.append(paragraph)
                current_tokens += paragraph_tokens
        else:
            current_chunk.append(paragraph)
            current_tokens += paragraph_tokens

    if current_chunk:
        chunks.append('\n\n'.join(current_chunk))

    return chunks

def is_valid_sentence(sentence):
    # Define a regex pattern for a valid sentence
    valid_pattern = r'^[A-Z].*'
    invalid_pattern_bar = r'\| *\|'
    invalid_pattern_doi = r'https://doi'

    is_valid = bool(re.match(valid_pattern, sentence))
    contains_invalid_bar = bool(re.search(invalid_pattern_bar, sentence))
    contains_invalid_doi = bool(re.search(invalid_pattern_doi, sentence))

    return is_valid and not (contains_invalid_bar or contains_invalid_doi)




def process_folder(folder_path,output_file):
    """
    Process all text files in the folder and chunk their contents.

    :param folder_path: Path to the folder containing documents.
    :param max_paragraphs: Maximum number of paragraphs per chunk.
    :param min_words: Minimum number of words required for a chunk.
    :return: List of text chunks.
    """
    results = []
    doc_id = 1
    for filename in os.listdir(folder_path):
        if filename.endswith('.txt') or filename.endswith('.md'):
            with open(os.path.join(folder_path, filename), 'r', encoding='utf-8') as file:
                text = file.read()
                doc_chunks = chunk_text_by_paragraph(text)
                for chunk in doc_chunks: 
                    results.append({'doc_id': doc_id, 'text': chunk, 'filename': filename})
                    doc_id += 1
    
    # Save the chunks to a new JSONL file
    with jsonlines.open(output_file, mode='w') as writer:
        writer.write_all(results)

    return results


if __name__ == "__main__":
    # Example usage
    folder_path = '../input/harryPotter'  # Replace with the path to your folder
    output_file = '../jsonl/raw.jsonl'

    process_folder(folder_path,output_file)

    print(f"Processed {len(chunks)} chunks and wrote to {output_file}")
