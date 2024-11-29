# src/vector_store.py
from langchain.vectorstores import Chroma 

class VectorStore:
    def __init__(self, embedding_function):
        self.db = Chroma(
            persist_directory="./vector_db",
            embedding_function=embedding_function
        )
    
    def add_texts(self, texts):
        try:
            self.db.add_documents(texts)
            self.db.persist()
        except Exception as e:
            raise Exception(f"Error adding texts to vector store: {str(e)}")
    
    def similarity_search(self, query, k=4):
        try:
            return self.db.similarity_search(query, k=k)
        except Exception as e:
            raise Exception(f"Error performing similarity search: {str(e)}")