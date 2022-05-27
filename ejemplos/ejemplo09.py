# Módulos necesarios:
# - requests
# - beautifulsoup
# - wget
#
# python3 -m pip install requests 
# python3 -m pip install beautifulsoup4
# python3 -m pip install wget

# Referencias:
# - https://requests.readthedocs.io/en/latest/
# - https://www.crummy.com/software/BeautifulSoup/bs4/doc/

# Importamos los módulos necesarios
import requests
from bs4 import BeautifulSoup
import wget

# Hacemos una petición HTTP a una URL
url = "https://www.marca.com"
page = requests.get(url)

# Convertimos la respuesta en un objeto BeautifulSoup
soup = BeautifulSoup(page.content, "html.parser")

# Obtenemos todos las etiquetas img del documento
imagenes = soup.find_all("img")

# Mostramos la lista de etiquetas img
#print(imagenes)

# Mostramos el texto que hay dentro de cada etiqueta a
# Utilizamos el método .strip() para eliminar los espacios en blanco al inicio y al final de la cadena
# Mostramos un número delante de cada imagen
for imagen in imagenes:
    try:
        print(f"{imagen['src']}")
        url_imagen = imagen['src']
        if url_imagen.endswith('.jpg') or url_imagen.endswith('.png'):
            wget.download(url_imagen)
    except KeyError:
        pass