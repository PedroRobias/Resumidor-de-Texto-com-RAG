def dividir_em_chunks(texto: str, tamanho: int = 400, sobreposicao: int = 50): #Divisão do texto em partes menores
    palavras = texto.split() 
    chunks = []

    inicio = 0
    while inicio < len(palavras):
        fim = inicio + tamanho
        chunk = " ".join(palavras[inicio:fim])
        chunks.append(chunk)
        inicio = fim - sobreposicao

    return chunks
