import spacy
import os
from pathlib import Path
import re

# Asegúrate de que spaCy y el modelo de lenguaje francés estén instalados:
# pip install spacy
# python -m spacy download fr_core_news_sm

def analyze_lexical_diversity(input_folder, output_file):
    # Cargar el modelo de lenguaje de spaCy
    nlp = spacy.load("fr_core_news_sm")

    # Crear una lista para almacenar los resultados
    results = []

    # Procesar cada archivo en la carpeta de entrada
    for document_name in sorted(os.listdir(input_folder), key=natural_keys):
        input_file_path = os.path.join(input_folder, document_name)
        document = os.path.splitext(document_name)[0]

        # Verificar si el archivo es un archivo de texto antes de procesarlo
        if input_file_path.lower().endswith('.txt'):
            with open(input_file_path, 'r', encoding='utf-8') as file_in:
                text = file_in.read()

            # Procesar el texto con spaCy
            doc = nlp(text)

            # Contar tokens y tipos
            tokens = [token.text for token in doc if not token.is_punct and not token.is_space]
            types = set(tokens)
            num_tokens = len(tokens)
            num_types = len(types)

            # Calcular TTR
            ttr = num_types / num_tokens if num_tokens > 0 else 0
            ttr_str = "{:.2f}".format(ttr).replace('.', ',')

            # Guardar los resultados
            results.append((document, num_types, num_tokens, ttr_str))

            print(f"TTR calculado para: {document}")

    # Escribir los resultados en un archivo de texto
    with open(output_file, 'w', encoding='utf-8') as file_out:
        # Escribir los datos en columnas verticales con un encabezado para cada sección
        file_out.write("Document\n")
        file_out.write("\n".join(result[0] for result in results) + "\n")
        file_out.write("Types\n")
        file_out.write("\n".join(str(result[1]) for result in results) + "\n")
        file_out.write("Tokens\n")
        file_out.write("\n".join(str(result[2]) for result in results) + "\n")
        file_out.write("TTR\n")
        file_out.write("\n".join(result[3] for result in results))

# Rutas de entrada y salida
input_folder = "C:\\Users\\34637\\Desktop\\git\\serie completa en bruto"
output_file = "C:\\Users\\34637\\Desktop\\git\\csv\\lexical_diversity_analysis.txt"

# Funciones auxiliares para el ordenamiento natural
def atoi(text):
    return int(text) if text.isdigit() else text

def natural_keys(text):
    return [ atoi(c) for c in re.split(r'(\d+)', text) ]

# Llamar a la función
analyze_lexical_diversity(input_folder, output_file)
