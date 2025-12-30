# Resumidor de Texto com RAG

Este projeto foi desenvolvido para fins acadêmicos e de aprendizado, com o objetivo de explorar conceitos fundamentais de Processamento de Linguagem Natural (PLN).

A proposta central do projeto é compreender, na prática, como funciona um sistema baseado em Retrieval-Augmented Generation (RAG), no qual um 
modelo de linguagem não responde apenas com base em conhecimento pré-treinado, mas sim a partir de informações recuperadas de um documento fornecido pelo usuário.

Todo o processamento é realizado localmente, sem dependência de APIs pagas.

O projeto foi feito como uma atividade de estudo e experimentação.


## ▶️ Como Executar o Projeto

Antes de tudo, clone o repositório: https://github.com/PedroRobias/Resumidor-de-Texto-com-RAG

```bash
python -m venv venv               # Criar ambiente virtual
venv\Scripts\activate             # Ativar ambiente
pip install -r requirements.txt   # Instala as dependências / bibliotecas
ollama pull phi3                  # Instala o modelo pré-treinada do Ollama
python main.py                    # Executa o main
