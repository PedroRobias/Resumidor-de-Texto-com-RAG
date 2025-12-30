from sentence_transformers import SentenceTransformer
import numpy as np


class EmbeddingGenerator:
    def __init__(self, model_name="all-MiniLM-L6-v2"):
        self.model = SentenceTransformer(model_name)

    def gerar_embeddings(self, textos: list[str]) -> np.ndarray:
        return self.model.encode(
            textos,
            convert_to_numpy=True,
            show_progress_bar=False
        ).astype("float32")
