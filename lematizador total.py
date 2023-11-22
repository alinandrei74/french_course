import os

# Definir el directorio de los archivos de la serie completa
source_directory = 'C:\\Users\\34637\\Desktop\\git\\serie completa'

# Definir el directorio donde se guardará el archivo unificado de lematizados
destination_directory = 'C:\\Users\\34637\\Desktop\\git\\lematizado total'

# Asegúrate de que el directorio de destino existe, si no, créalo
os.makedirs(destination_directory, exist_ok=True)

# Definir el nombre y la ruta del archivo de salida
output_filename = 'combined_lematizados.txt'
output_filepath = os.path.join(destination_directory, output_filename)

# Crear o sobrescribir el archivo de salida
with open(output_filepath, 'w', encoding='utf-8') as outfile:
    # Listar todos los archivos en el directorio de origen que sean archivos .txt
    # y asegurarse de que están en orden numérico basado en el nombre del archivo
    file_list = sorted(
        (f for f in os.listdir(source_directory) if f.startswith('documento') and f.endswith('.txt')),
        key=lambda x: int(x.partition('documento')[2].partition('.txt')[0])
    )

    for i, filename in enumerate(file_list):
        # Construir la ruta completa del archivo actual
        filepath = os.path.join(source_directory, filename)
        
        # Asegurarse de que es un archivo y no un directorio/folder
        if os.path.isfile(filepath):
            with open(filepath, 'r', encoding='utf-8') as readfile:
                outfile.write(readfile.read())  # Escribir el contenido en el archivo de salida
                
            # Añadir una línea de guiones después de cada archivo excepto después del último
            if i < len(file_list) - 1:  # No añadir guiones después del último archivo
                outfile.write('\n' + '-' * 40 + '\n')

print(f'Todos los archivos han sido combinados en {output_filepath}')
