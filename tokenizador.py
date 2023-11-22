import spacy
import os
import string

# Cargar el modelo de spaCy para francés
nlp = spacy.load('fr_core_news_sm')

# Función para tokenizar el texto y asignar un valor numérico a cada token
def tokenize_and_convert_to_numeric(text, token_map):
    # Procesar el texto con spaCy para tokenizar y lematizar
    doc = nlp(text)
    # Reemplazar cada token por su valor numérico, utilizando el lema del token
    numeric_text = ' '.join(str(token_map.setdefault(token.lemma_, len(token_map) + 1)) for token in doc)
    return numeric_text

# Directorio de archivos originales y de destino
source_directory = "C:\\Users\\34637\\Desktop\\git\\serie completa"
destination_directory = "C:\\Users\\34637\\Desktop\\git\\tokenizados serie completa"

# Crear el directorio de destino si no existe
os.makedirs(destination_directory, exist_ok=True)

# Función para procesar archivos en el directorio dado
def process_files(source_directory, destination_directory):
    # Mapa para almacenar la asignación única de números a tokens
    token_map = {}
    # Obtener una lista de archivos en el directorio fuente
    for filename in os.listdir(source_directory):
        if filename.endswith('.txt'):  # Procesar solo archivos .txt
            source_file_path = os.path.join(source_directory, filename)
            destination_file_path = os.path.join(destination_directory, filename)
            
            with open(source_file_path, 'r', encoding='utf-8') as file:
                text = file.read()
            
            # Tokenizar y convertir el texto a valores numéricos
            numeric_text = tokenize_and_convert_to_numeric(text, token_map)
            
            # Guardar el texto convertido a numérico
            with open(destination_file_path, 'w', encoding='utf-8') as file:
                file.write(numeric_text)

# Ejecutar la función de procesamiento de archivos
process_files(source_directory, destination_directory)
