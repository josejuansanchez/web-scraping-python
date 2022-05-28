# Importamos los módulos necesarios
import requests
from bs4 import BeautifulSoup
import wget
import os

#-------------------------------------------------------------------------------
# Funciones

# Función: descargar_imagenes
# Entrada:
# - url         URL del sitio web donde vamos a descargar las imágenes
# - width       Solo vamos a descargar las imágenes que tengan este ancho
# - height      Solo vamos a descargar las imágenes que tengan este alto
# - directorio  Path del directorio donde vamos a descargar las imágenes

def descargar_imagenes(url, width, height, directorio):
    # Hacemos una petición HTTP a una URL
    page = requests.get(url)

    # Convertimos la respuesta en un objeto BeautifulSoup
    soup = BeautifulSoup(page.content, "html.parser")

    # Obtenemos todos las etiquetas img del documento
    imagenes = soup.find_all("img")

    # Comprobamos si existe el directorio y si no existe lo creamos
    if os.path.exists(directorio) == False:
        os.mkdir(directorio)

    for imagen in imagenes:
        try:
            # Si los atributos width y height no son los esperados entonces
            # saltamos a la siguiente iteración del bucle
            if imagen['width'] != width or imagen['height'] != height:
                continue

            print(f"src: {imagen['src']}")
            print(f"width: {imagen['width']} - height: {imagen['height']}")

            # Solo descargamos imágenes con extensión .jpg o .png
            if imagen['src'].endswith('.jpg') or imagen['src'].endswith('.png'):
                print("Descargando imagen...")
                wget.download(imagen['src'], out=directorio)
        except KeyError:
            pass

#-------------------------------------------------------------------------------
# Programa Principal

url = "https://www.diariodealmeria.es"
width = "142"
height = "90"
directorio = "descargas"

descargar_imagenes(url, width, height, directorio)