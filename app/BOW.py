import os
import pandas as pd
from collections import Counter

def make_vocab(path):

    path = os.path.abspath(path)

    if not os.path.exists(path):
        raise FileNotFoundError(f"El directorio no existe: {path}")

    vocab = set()
    txt_files = [f for f in os.listdir(path) if f.endswith(".txt")]

    if not txt_files:
        raise FileNotFoundError(f"No se encontraron archivos .txt en: {path}")

    for file in txt_files:
        file_path = os.path.join(path, file)

        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()
            words = content.split()
            vocab.update(words)
        print(f"Procesado: {file}")

    vocab = sorted(vocab)
    print(f"\nTamaño del vocabulario: {len(vocab)} palabras únicas")
    return vocab

def make_bow(path, vocab):

    path = os.path.abspath(path)

    txt_files = [f for f in os.listdir(path) if f.endswith(".txt")]
    if not txt_files:
        raise FileNotFoundError(f"No se encontraron archivos .txt en: {path}")

    docs = []

    for file in txt_files:
        file_path = os.path.join(path, file)
        with open(file_path, "r", encoding="utf-8") as f:
            words = f.read().split()

        counter = Counter(words)

        vector = [counter.get(word, 0) for word in vocab]

        docs.append(vector)

    bow_df = pd.DataFrame(docs, columns=vocab, index=txt_files)

    print(f"Matriz Bag-of-Words creada con tamaño {bow_df.shape}")
    return bow_df

