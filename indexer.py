from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

MODEL_NAME = "all-MiniLM-L6-v2"

class Indexer:
    def __init__(self):
        self.embedder = SentenceTransformer(MODEL_NAME)
        self.index = None
        self.metadatas = []

    def build(self, docs):
        texts = [d["text"] for d in docs]
        self.metadatas = [d["source"] for d in docs]
        embeddings = self.embedder.encode(texts, show_progress_bar=True)
        dim = embeddings.shape[1]
        self.index = faiss.IndexFlatL2(dim)
        self.index.add(np.array(embeddings, dtype="float32"))

    def query(self, q, top_k=5):
        q_emb = self.embedder.encode([q])
        D, I = self.index.search(np.array(q_emb, dtype="float32"), top_k)
        return [self.metadatas[i] for i in I[0]], [D[0][j] for j in range(len(I[0]))]
