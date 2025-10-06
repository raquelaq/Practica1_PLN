import re
import os
from docx import Document

def load_stopwords(stopwords_path):
    """Carga las stopwords desde un archivo de texto (una por línea)."""
    with open(stopwords_path, 'r', encoding="utf-8") as f:
        return set([line.strip().lower() for line in f if line.strip()])

def preprocess_docx(input_path, output_path, stopwords_path):
    """Preprocesa documentos .docx en un directorio y guarda el texto limpio en .txt."""

    input_path = os.path.abspath(input_path)
    output_path = os.path.abspath(output_path)
    stopwords_path = os.path.abspath(stopwords_path)

    os.makedirs(input_path, exist_ok=True)
    os.makedirs(output_path, exist_ok=True)

    stopwords = load_stopwords(stopwords_path)

    print(f"\n Directorio de entrada: {input_path}")
    print(f"Directorio de salida: {output_path}\n")

    for file in os.listdir(input_path):
        if file.endswith('.docx'):
            file_path = os.path.join(input_path, file)

            doc = Document(file_path)
            text = " ".join([p.text for p in doc.paragraphs])

            text = text.lower()

            text = re.sub(r"[^a-záéíóúüñ\s]", " ", text)

            words = text.split()
            filtered_words = [w for w in words if w not in stopwords]

            clean_text = " ".join(filtered_words)

            output_name = os.path.splitext(file)[0] + "_preprocessed.txt"
            output_file_path = os.path.join(output_path, output_name)

            with open(output_file_path, "w", encoding="utf-8") as f:
                f.write(clean_text)

            print(f"Procesado: {file} → {output_name}")

    print("\nPreprocesamiento completado.\n")
