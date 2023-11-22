import os

# Establece el directorio de trabajo donde están los documentos originales
source_directory = 'C:\\Users\\34637\\Desktop\\git\\tokenizados serie completa'  # Cambia esto por tu directorio real de documentos

# El nombre del directorio donde se guardará el documento combinado
destination_directory = 'C:\\Users\\34637\\Desktop\\git\\tokenizado total'  # Directorio de destino para el archivo combinado

# Asegúrate de que el directorio de destino existe, si no, créalo
os.makedirs(destination_directory, exist_ok=True)

# El nombre del archivo combinado resultante
combined_filename = 'combined_document.txt'

# La ruta completa al archivo combinado
combined_filepath = os.path.join(destination_directory, combined_filename)

# Abre el archivo combinado en modo de escritura
with open(combined_filepath, 'w', encoding='utf-8') as combined_file:
    # Itera sobre el rango de números de tus documentos
    for i in range(1, 62):  # Asegúrate de que el rango coincida con tus números de documento
        # Construye el nombre del archivo actual
        current_filename = f'documento{i}.txt'
        # La ruta completa al archivo actual
        current_filepath = os.path.join(source_directory, current_filename)
        
        # Verifica si el archivo actual existe para evitar errores
        if os.path.isfile(current_filepath):
            # Abre el documento actual y lee su contenido
            with open(current_filepath, 'r', encoding='utf-8') as current_file:
                content = current_file.read()
                # Escribe el contenido al archivo combinado
                combined_file.write(content)
                # Escribe una línea de guiones después de cada sección de contenido si no es el último documento
                if i < 61:  # Cambia el 61 al número de tu último documento si es diferente
                    combined_file.write('\n' + '-' * 40 + '\n')

print(f"Todos los documentos han sido combinados en {combined_filename}")
