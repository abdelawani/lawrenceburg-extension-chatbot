from langchain.vectorstores import FAISS
from langchain.embeddings.openai import OpenAIEmbeddings

def build_vector_store(documents):
    embedder = OpenAIEmbeddings()
    return FAISS.from_documents(documents, embedder)

def retrieve_documents(db, query, k=4):
    return db.similarity_search(query, k=k)
