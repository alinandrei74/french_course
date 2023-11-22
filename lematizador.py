import spacy
import os
import string
import re  # Importa el módulo de expresiones regulares

# Cargar el modelo de spaCy para francés
nlp = spacy.load('fr_core_news_sm')

# Función para limpiar y lematizar el texto
def clean_and_lemmatize(text):
    # Usar regex para eliminar dígitos pegados a las palabras
    text = re.sub(r'\w*\d\w*', '', text)  # Elimina palabras que contienen números
    # Convertir a minúsculas y eliminar puntuación
    text = text.lower().translate(str.maketrans('', '', string.punctuation))
    # Procesar el texto con spaCy
    doc = nlp(text)
    # Extraer los lemas de cada token en el documento
    lemmatized_text = ' '.join(token.lemma_ for token in doc if not token.is_punct and not token.is_space)
    return lemmatized_text

# Directorio de archivos originales y de destino
source_directory = "C:\\Users\\34637\\Desktop\\git\\nivel1"
destination_directory = "C:\\Users\\34637\\Desktop\\git\\lematizados nivel1"

# Crear el directorio de destino si no existe
os.makedirs(destination_directory, exist_ok=True)

# Función auxiliar para determinar la clave de ordenamiento
def sort_key(filename):
    # Intentar extraer el número al principio del nombre del archivo
    # y devolverlo para la ordenación
    parts = filename.split('.')[0]
    if parts.isdigit():
        return int(parts)
    return float('inf'), filename  # Coloca los archivos no numéricos al final

# Función para procesar archivos en el directorio dado
def process_files(source_directory, destination_directory):
    # Obtener una lista de archivos y ordenarla
    files = sorted(os.listdir(source_directory), key=sort_key)
    # Filtrar solo archivos .txt
    text_files = filter(lambda f: f.endswith('.txt'), files)
    for filename in text_files:
        source_file_path = os.path.join(source_directory, filename)
        destination_file_path = os.path.join(destination_directory, filename)
        
        with open(source_file_path, 'r', encoding='utf-8') as file:
            text = file.read()
        
        # Lematizar y limpiar el contenido del archivo
        lemmatized_text = clean_and_lemmatize(text)
        
        # Guardar el texto lematizado
        with open(destination_file_path, 'w', encoding='utf-8') as file:
            file.write(lemmatized_text)

# Ejecutar la función de procesamiento de archivos
process_files(source_directory, destination_directory)
