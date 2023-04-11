import os
import random
import string

# Función para generar un nombre aleatorio
def generar_nombre_aleatorio(n):
    caracteres = string.ascii_letters + string.digits
    return ''.join(random.choice(caracteres) for _ in range(n))

# Directorio donde se crearán las carpetas
directorio_base = "./carpetas/"

# Número de carpetas a crear
num_carpetas = 56

# Contenido del archivo index.html
contenido_html = f'''
<!DOCTYPE html>
<html>
<head>
<title>Boleto</title>
</head>
<body>
<h1>Bienvenido a mi página</h1>
<p>Esta es una página generada automáticamente.</p>
</body>
</html>
'''

# Lista para almacenar los nombres de las carpetas generadas
nombres_carpetas = []

# Crear las carpetas con nombres aleatorios y archivos index.html
for i in range(num_carpetas):
    contenido_html = f'''
    <!DOCTYPE html>
    <html>
    <head>
    <title>Boleto {i+1}</title>
    <style>
    body {{
    background-color: black;
    color: white;
    font-family: 'Helvetica', sans-serif;
    font-size: 24px;
    padding: 20px;
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100vh;
    }}

    .animacion {{
        animation: fadein 3s;
    }}

    @keyframes fadein {{
        from {{
            opacity: 0;
        }}
        to {{
            opacity: 1;
        }}
    }}
    </style>
    </head>
    <body>
    <div class="animacion">
    <h1>Bienvenido, tu boleto es el {i+1}</h1>
    </div>
    </body>
    </html>
    '''
    nombre_carpeta = generar_nombre_aleatorio(10)  # Generar un nombre aleatorio de 10 caracteres
    ruta_carpeta = os.path.join(directorio_base, nombre_carpeta)
    os.makedirs(ruta_carpeta)
    ruta_archivo_html = os.path.join(ruta_carpeta, "index.html")
    with open(ruta_archivo_html, "w") as archivo_html:
        archivo_html.write(contenido_html)
    nombres_carpetas.append("https://silvestrerosales.github.io/carpetas/"+nombre_carpeta+"/")

# Crear archivo de texto con los nombres de las carpetas generadas
ruta_archivo_txt = os.path.join(directorio_base, "nombres_carpetas.txt")
with open(ruta_archivo_txt, "w") as archivo_txt:
    archivo_txt.write("\n".join(nombres_carpetas))

print(f"Se han creado {num_carpetas} carpetas en '{directorio_base}' con archivos index.html.")
print(f"Se ha creado el archivo '{ruta_archivo_txt}' con los nombres de las carpetas generadas.")
