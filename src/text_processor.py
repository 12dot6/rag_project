# src/text_processor.py
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from typing import List

class TextProcessor:
    def __init__(self):
        self.text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000,
            chunk_overlap=200,
            length_function=len
        )
        self.embeddings = OpenAIEmbeddings()
    
    def process_documents(self, documents: List):
        try:
            texts = self.text_splitter.split_documents(documents)
            return texts
        except Exception as e:
            raise Exception(f"Error processing documents: {str(e)}")