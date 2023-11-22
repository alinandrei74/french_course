import spacy
import os
from pathlib import Path
import re

# Asegúrate de que spaCy y el modelo de lenguaje francés estén instalados:
# pip install spacy
# python -m spacy download fr_core_news_sm

# Función auxiliar para realizar el ordenamiento natural de los nombres de los archivos
def atoi(text):
    return int(text) if text.isdigit() else text

def natural_keys(text):
    return [ atoi(c) for c in re.split(r'(\d+)', text) ]

def analyze_documents(input_folder, output_file):
    # Cargar el modelo de lenguaje de spaCy
    nlp = spacy.load("fr_core_news_sm")

    # Lista para almacenar los nombres de los archivos y sus datos correspondientes
    data = []

    # Procesar cada archivo en la carpeta de entrada y almacenar los resultados
    for document_name in sorted(os.listdir(input_folder), key=natural_keys):
        input_file_path = os.path.join(input_folder, document_name)

        # Verificar si el archivo es un archivo de texto antes de procesarlo
        if input_file_path.lower().endswith('.txt'):
            with open(input_file_path, 'r', encoding='utf-8') as file_in:
                text = file_in.read()

            # Procesar el texto con spaCy
            doc = nlp(text)

            # Contar las oraciones y calcular la longitud media de la frase
            sentences = list(doc.sents)
            num_sentences = len(sentences)
            total_length = sum(len(sentence.text.split()) for sentence in sentences)
            avg_sentence_length = total_length / num_sentences if num_sentences > 0 else 0

            # Reemplazar el punto por una coma para la longitud media de la frase
            avg_sentence_length_str = f"{avg_sentence_length:.2f}".replace('.', ',')

            # Agregar los resultados a la lista
            data.append((os.path.splitext(document_name)[0], num_sentences, avg_sentence_length_str))

            print(f"Análisis completado para: {document_name}")

    # Abrir el archivo de texto de salida para escritura
    with open(output_file, 'w', encoding='utf-8') as file_out:
        # Escribir los resultados en el archivo de texto de salida
        file_out.write("Document\n")
        file_out.write("\n".join(item[0] for item in data) + "\n")
        file_out.write("Number of Sentences\n")
        file_out.write("\n".join(str(item[1]) for item in data) + "\n")
        file_out.write("Average Sentence Length\n")
        file_out.write("\n".join(item[2] for item in data))

# Rutas de entrada y salida
input_folder = "C:\\Users\\34637\\Desktop\\git\\serie completa en bruto"
output_file = "C:\\Users\\34637\\Desktop\\git\\csv\\document_analysis.txt"

# Llamar a la función
analyze_documents(input_folder, output_file)
