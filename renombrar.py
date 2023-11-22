import os

# Definir el directorio donde están los archivos de la segunda serie
directory = "C:\\Users\\34637\\Desktop\\git\\serie completa"

# Definir el incremento para la numeración de los archivos
increment = 31

# Obtener una lista de todos los archivos de texto en el directorio
files = [f for f in os.listdir(directory) if f.endswith('.txt') and f.startswith('documento')]

# Ordenar los archivos por su número actual para no tener conflictos al renombrarlos
files.sort(key=lambda x: int(x.replace('documento', '').replace('.txt', '')))

# Cambiar el nombre de los archivos incrementando su numeración
for filename in files:
    # Extraer el número del nombre del archivo
    number = int(filename.replace('documento', '').replace('.txt', ''))
    # Crear el nuevo nombre del archivo con el número incrementado
    new_number = number + increment
    new_filename = f"documento{new_number}.txt"
    
    # Crear rutas completas de archivo antiguo y nuevo
    old_filepath = os.path.join(directory, filename)
    new_filepath = os.path.join(directory, new_filename)
    
    # Renombrar el archivo
    os.rename(old_filepath, new_filepath)

print("Renombramiento completado.")
