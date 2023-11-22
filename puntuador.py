import spacy
import os
from pathlib import Path
import re  # Import the regex module to use for number cleaning

# Asegúrate de que spaCy y el modelo de lenguaje francés estén instalados:
# pip install spacy
# python -m spacy download fr_core_news_sm

def clean_text(text):
    # Eliminar caracteres numéricos que puedan estar pegados a palabras o entre espacios
    text = re.sub(r'\w*\d\w*', '', text).strip()
    return text

def clean_and_save_documents(input_folder, output_folder):
    # Cargar el modelo de lenguaje de spaCy
    nlp = spacy.load("fr_core_news_sm")

    # Asegurarse de que la carpeta de salida existe
    Path(output_folder).mkdir(parents=True, exist_ok=True)
    
    # Procesar cada archivo en la carpeta de entrada
    for document_name in os.listdir(input_folder):
        input_file_path = os.path.join(input_folder, document_name)
        output_file_path = os.path.join(output_folder, document_name)
        
        # Verificar si el archivo es un archivo de texto antes de procesarlo
        if input_file_path.lower().endswith('.txt'):
            # Leer el contenido del archivo
            with open(input_file_path, 'r', encoding='utf-8') as file:
                text = file.read()
            
            # Limpiar el texto de números
            cleaned_text = clean_text(text)

            # Procesar el texto limpio con spaCy
            doc = nlp(cleaned_text)
            sentences = [sent.text.strip() for sent in doc.sents]
            
            # Unir las oraciones procesadas en un solo texto
            cleaned_output = ' '.join(sentences)
            
            # Guardar el texto limpiado en la carpeta de salida
            with open(output_file_path, 'w', encoding='utf-8') as file:
                file.write(cleaned_output)
            
            print(f"Archivo procesado y guardado: {output_file_path}")

# Uso de la función con las rutas de las carpetas correspondientes
input_folder = "C:\\Users\\34637\\Desktop\\git\\serie completa en bruto"  # Cambia esto por la ruta de tu carpeta de entrada
output_folder = "C:\\Users\\34637\\Desktop\\git\\puntuados"  # Cambia esto por la ruta de tu carpeta de salida

clean_and_save_documents(input_folder, output_folder)
