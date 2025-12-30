import requests
import json

class SintetizadorPhi:
    def __init__(self, model="phi3"):
        self.model = model
        self.url = "http://localhost:11434/api/generate"

    def resumir(self, contexto: str, pergunta: str) -> str:
        prompt = f"""
Use apenas o contexto para responder à pergunta.

Contexto:
{contexto}

Pergunta:
{pergunta}
"""

        response = requests.post(
            self.url,
            json={
                "model": self.model,
                "prompt": prompt,
                "stream": True
            },
            stream=True
        )

        resposta_final = ""

        for linha in response.iter_lines():
            if linha:
                data = json.loads(linha.decode("utf-8"))
                resposta_final += data.get("response", "")

        return resposta_final.strip()
