from setuptools import setup, find_packages

setup(
    name="rag_project",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        'streamlit',
        'langchain',
        'openai',
        'chromadb',
        'unstructured',
        'pandas',
        'python-docx',
        'PyPDF2',
        'python-dotenv'
    ],
)