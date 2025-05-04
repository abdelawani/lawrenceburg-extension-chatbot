from langchain.vectorstores import FAISS
from langchain.embeddings import OpenAIEmbeddings

def build_vector_store(documents):
    embedder = OpenAIEmbeddings()
    db = FAISS.from_documents(documents, embedder)
    return db

def retrieve_documents(db, query, k=4):
    return db.similarity_search(query, k=k)
