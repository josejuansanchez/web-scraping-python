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

# Mostramos el contenido del objeto BeautifulSoup
print(soup.prettify())