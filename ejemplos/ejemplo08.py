# Módulos necesarios:
# - requests
# - beautifulsoup
#
# python3 -m pip install requests 
# python3 -m pip install beautifulsoup4

# Referencias:
# - https://requests.readthedocs.io/en/latest/
# - https://www.crummy.com/software/BeautifulSoup/bs4/doc/

# Importamos los módulos necesarios
import requests
from bs4 import BeautifulSoup

# Hacemos una petición HTTP a una URL
url = "https://www.marca.com"
page = requests.get(url)

# Mostramos el contenido de la respuesta
#print(page.text)

# Convertimos la respuesta en un objeto BeautifulSoup
soup = BeautifulSoup(page.content, "html.parser")

# Obtenemos todos las etiquetas img del documento
imagenes = soup.find_all("img")

# Mostramos la lista de etiquetas img
#print(imagenes)

# Mostramos el texto que hay dentro de cada etiqueta a
# Utilizamos el método .strip() para eliminar los espacios en blanco al inicio y al final de la cadena
# Mostramos un número delante de cada imagen

count = 1
for imagen in imagenes:
    try:
        print(f"{count}. {imagen['src']} {imagen['alt']}")
        #print(f"{count}. {imagen.get('src')} {imagen.get('alt')}")
        count = count + 1
    except KeyError:
        pass