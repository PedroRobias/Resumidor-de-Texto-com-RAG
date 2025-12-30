from pathlib import Path

#Leitura do Arquivo em String

def carregar_texto(caminho: str) -> str:
    path = Path(caminho)
    with path.open("r", encoding="utf-8") as f:
        return f.read()
