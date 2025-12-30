import faiss
import numpy as np


class RetrieverFAISS:
    def __init__(self, embeddings: np.ndarray):
        dim = embeddings.shape[1]
        self.index = faiss.IndexFlatL2(dim)
        self.index.add(embeddings)

    def buscar(self, query_embedding: np.ndarray, k: int = 3):
        _, indices = self.index.search(query_embedding, k)
        return indices[0]
