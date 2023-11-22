import spacy
import csv
from pathlib import Path

# Función para cargar el diccionario de frecuencias desde un archivo CSV
def load_frequency_dictionary(csv_file_path):
    frequency_dict = {}
    with open(csv_file_path, mode='r', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            frequency_dict[row['lemme'].lower()] = int(row['freq'])
    return frequency_dict

# Función para procesar los documentos y generar los CSVs solicitados
def process_documents(input_folder, frequency_dict, output_folder):
    # Cargar el modelo de spaCy para francés
    nlp = spacy.load("fr_core_news_sm")

    # Archivos de salida
    frequencies_output_path = Path(output_folder) / "frecuencias_palabras.csv"
    missing_output_path = Path(output_folder) / "lemas_ausentes.csv"

    with open(frequencies_output_path, 'w', encoding='utf-8', newline='') as freq_file, \
         open(missing_output_path, 'w', encoding='utf-8', newline='') as miss_file:

        freq_writer = csv.writer(freq_file)
        miss_writer = csv.writer(miss_file)
        
        # Escribir los encabezados de los archivos CSV
        freq_writer.writerow(["Documento", "Frecuencias"])
        miss_writer.writerow(["Documento", "Lemas ausentes"])

        for document_path in Path(input_folder).glob('*.txt'):
            with open(document_path, 'r', encoding='utf-8') as file:
                text = file.read()
                doc = nlp(text)

                # Preparar listas para almacenar frecuencias y lemas ausentes
                frequencies = []
                missing_lemmas = []

                # Procesar el texto y recopilar datos
                for token in doc:
                    if token.is_alpha:
                        lemma = token.lemma_.lower()
                        if lemma in frequency_dict:
                            frequencies.append(frequency_dict[lemma])
                        else:
                            missing_lemmas.append(lemma)

                # Escribir frecuencias y lemas ausentes en sus respectivos archivos
                freq_writer.writerow([document_path.stem] + frequencies)
                if missing_lemmas:  # Solo escribir si hay lemas ausentes
                    miss_writer.writerow([document_path.stem] + list(set(missing_lemmas)))  # Eliminar duplicados

                print(f"Procesado: {document_path.name}")

# Rutas de archivos y carpetas
input_folder = "C:\\Users\\34637\\Desktop\\git\\serie completa"
frequency_dict = load_frequency_dictionary("C:\\Users\\34637\\Desktop\\git\\csv\\frecuencia_fr.csv")
output_folder = "C:\\Users\\34637\\Desktop\\git\\csv"

# Procesar documentos
process_documents(input_folder, frequency_dict, output_folder)
