# src/document_processor.py
import os
# type: ignore
from langchain.document_loaders import PyPDFLoader, Docx2txtLoader, UnstructuredExcelLoader 
from typing import List

class DocumentProcessor:
    def __init__(self):
        self.supported_formats = {
            '.pdf': PyPDFLoader,
            '.docx': Docx2txtLoader,
            '.xlsx': UnstructuredExcelLoader
        }
    
    def load_document(self, file_path: str):
        try:
            file_extension = os.path.splitext(file_path)[1].lower()
            if file_extension in self.supported_formats:
                loader = self.supported_formats[file_extension](file_path)
                return loader.load()
            else:
                raise ValueError(f"Unsupported file format: {file_extension}")
        except Exception as e:
            raise Exception(f"Error loading document: {str(e)}")