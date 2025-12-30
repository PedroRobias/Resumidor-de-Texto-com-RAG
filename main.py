from src.chunking import dividir_em_chunks
from src.embedding import EmbeddingGenerator
from src.retriever import RetrieverFAISS
from src.sintetizar import SintetizadorPhi


def main():
    with open("data/textoexemplo.txt", "r", encoding="utf-8") as f:
        texto = f.read()

    pergunta = "Cite espécies endêmicas da Caatinga"

    # 1. Chunking
    chunks = dividir_em_chunks(texto)

    # 2. Embeddings
    embedder = EmbeddingGenerator()
    chunk_embeddings = embedder.gerar_embeddings(chunks)

    # 3. Retriever (RAG)
    retriever = RetrieverFAISS(chunk_embeddings)
    pergunta_embedding = embedder.gerar_embeddings([pergunta])
    indices = retriever.buscar(pergunta_embedding, k=3)

    contexto_relevante = "\n".join([chunks[i] for i in indices])

    # 4. Síntese com LLM
    sintetizador = SintetizadorPhi()
    resposta = sintetizador.resumir(contexto_relevante, pergunta)

    print("\nResposta final:\n")
    print(resposta)


if __name__ == "__main__":
    main()
