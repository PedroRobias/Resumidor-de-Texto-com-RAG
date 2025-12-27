from src.carregar import load_text

text = load_text("data/documentos.txt")

print("Tamanho:", len(text))
print(text[:200])