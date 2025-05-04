from langchain.vectorstores import Chroma
from langchain.embeddings.openai import OpenAIEmbeddings

def build_vector_store(documents):
    embedder = OpenAIEmbeddings()
    return Chroma.from_documents(documents, embedder)

def retrieve_documents(db, query, k=4):
    return db.similarity_search(query, k=k)
