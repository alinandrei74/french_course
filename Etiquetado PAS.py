import spacy

# Cargar el modelo de spaCy para francés
nlp = spacy.load('fr_core_news_sm')

# Define las rutas a los archivos de origen y destino
source_filepath = 'C:\\Users\\34637\\Desktop\\git\\lematizado total\\combined_lematizados.txt'
output_filepath = 'C:\\Users\\34637\\Desktop\\git\\Etiquetado POS total\\lematizados_POS.txt'

# Crear o sobrescribir el archivo de salida
with open(source_filepath, 'r', encoding='utf-8') as infile, open(output_filepath, 'w', encoding='utf-8') as outfile:
    # Leer el archivo de origen por secciones
    sections = infile.read().split('-' * 40)  # Asumiendo que cada sección está separada por 40 guiones

    for section in sections:
        if section.strip():  # Verificar si la sección contiene texto y no solo espacios en blanco o saltos de línea
            # Procesar la sección con spaCy para obtener las etiquetas POS
            doc = nlp(section)
            # Escribir las etiquetas POS al archivo de salida, seguidas de un espacio
            for token in doc:
                if not token.is_punct and not token.is_space:  # Ignorar puntuación y espacios
                    outfile.write(token.pos_ + ' ')
            # Después de cada sección, escribe el delimitador de sección
            outfile.write('\n' + '-' * 40 + '\n')

print(f'El archivo con etiquetas POS ha sido creado en {output_filepath}')
