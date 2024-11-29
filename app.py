# app.py
import streamlit as st 
st.set_page_config(layout="wide")  # Ensures proper layout
import os
from dotenv import load_dotenv # type: ignore
from src.rag_system import RAGSystem

# Load environment variables
load_dotenv()

def create_app():
    st.title("Document Q&A System")
    
    # Initialize RAG system
    if 'rag_system' not in st.session_state:
        st.session_state.rag_system = RAGSystem()
    
    # File upload
    uploaded_file = st.file_uploader("Upload a document", type=['pdf', 'docx', 'xlsx'])
    if uploaded_file:
        with st.spinner("Processing document..."):
            try:
                # Save uploaded file temporarily
                with open(f"temp_{uploaded_file.name}", "wb") as f:
                    f.write(uploaded_file.getbuffer())
                st.session_state.rag_system.process_file(f"temp_{uploaded_file.name}")
                os.remove(f"temp_{uploaded_file.name}")
                st.success("Document processed successfully!")
            except Exception as e:
                st.error(f"Error processing document: {str(e)}")
    
    # Query input
    query = st.text_input("Ask a question about your documents:")
    if query:
        with st.spinner("Generating answer..."):
            try:
                response = st.session_state.rag_system.query(query)
                st.write(response['answer'])
            except Exception as e:
                st.error(f"Error generating response: {str(e)}")

if __name__ == "__main__":
    create_app()