from src.role_answer import process_role_answer
from src.passage_embedding import save_embedding_to_milvus

if __name__ == "__main__":

    # generate target entity type
    #process_role_answer()

    # save passage embedding to milvus
    document_collection_name = "graphrag_document_collection"
    save_embedding_to_milvus(document_collection_name)
   

