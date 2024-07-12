import os
import json

def chunk_text_by_paragraph(text, max_paragraphs=3):
    """
    Chunk text by paragraphs.

    :param text: The input text to chunk.
    :param max_paragraphs: Maximum number of paragraphs per chunk.
    :return: List of text chunks.
    """
    paragraphs = text.split('\n\n')
    chunks = ['\n\n'.join(paragraphs[i:i + max_paragraphs]) for i in range(0, len(paragraphs), max_paragraphs)]
    return chunks

def count_words(text):
    """
    Count the number of words in a string.

    :param text: The input text.
    :return: Word count of the text.
    """
    words = text.split()
    return len(words)

def process_folder(folder_path, max_paragraphs=3, min_words=100):
    """
    Process all text files in the folder and chunk their contents.

    :param folder_path: Path to the folder containing documents.
    :param max_paragraphs: Maximum number of paragraphs per chunk.
    :param min_words: Minimum number of words required for a chunk.
    :return: List of text chunks.
    """
    chunks = []
    for filename in os.listdir(folder_path):
        if filename.endswith('.txt') or filename.endswith('.md'):
            with open(os.path.join(folder_path, filename), 'r', encoding='utf-8') as file:
                text = file.read()
                doc_chunks = chunk_text_by_paragraph(text, max_paragraphs)
                filtered_chunks = [chunk for chunk in doc_chunks if count_words(chunk) >= min_words]
                chunks.extend(filtered_chunks)
    return chunks

def write_chunks_to_jsonl(chunks, filename):
    """
    Write text chunks to a jsonl file with incrementing keys.

    :param chunks: List of text chunks.
    :param filename: The name of the jsonl file to write to.
    """
    with open(filename, 'w') as f:
        for i, chunk in enumerate(chunks):
            doc_key = f'doc{i + 1}'
            json_line = json.dumps({doc_key: chunk})
            f.write(json_line + '\n')

# Example usage
folder_path = '../input'  # Replace with the path to your folder
output_file = 'output.jsonl'
max_paragraphs = 3  # Adjust this value as needed

chunks = process_folder(folder_path, max_paragraphs)
write_chunks_to_jsonl(chunks, output_file)

print(f"Processed {len(chunks)} chunks and wrote to {output_file}")
