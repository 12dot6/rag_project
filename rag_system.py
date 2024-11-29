# src/rag_system.py
from langchain.chat_models import ChatOpenAI 
from langchain.chains import ConversationalRetrievalChain 
from langchain.memory import ConversationBufferMemory 
from .document_processor import DocumentProcessor
from .text_processor import TextProcessor
from .vector_store import VectorStore

class RAGSystem:
    def __init__(self):
        self.llm = ChatOpenAI(temperature=0.7)
        self.doc_processor = DocumentProcessor()
        self.text_processor = TextProcessor()
        self.vector_store = VectorStore(self.text_processor.embeddings)
        
        self.qa_chain = ConversationalRetrievalChain.from_llm(
            llm=self.llm,
            retriever=self.vector_store.db.as_retriever(),
            memory=ConversationBufferMemory(
                memory_key="chat_history",
                return_messages=True
            )
        )
    
    def process_file(self, file_path):
        try:
            documents = self.doc_processor.load_document(file_path)
            texts = self.text_processor.process_documents(documents)
            self.vector_store.add_texts(texts)
        except Exception as e:
            raise Exception(f"Error processing file: {str(e)}")
    
    def query(self, question: str):
        try:
            return self.qa_chain({"question": question})
        except Exception as e:
            raise Exception(f"Error processing query: {str(e)}")