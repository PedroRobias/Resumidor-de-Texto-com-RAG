import numpy as np
import pandas as pd
import torch
import faiss
from sentence_transformers import SentenceTransformer
from transformers import pipeline

print("NumPy OK")
print("Pandas OK")
print("Torch OK")
print("FAISS OK")

model = SentenceTransformer("all-MiniLM-L6-v2")
print("SentenceTransformer OK")

summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
print("Transformers (summarizer) OK")