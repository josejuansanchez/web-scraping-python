# Módulos necesarios:
# - requests
#
# python3 -m pip install requests 

# Referencias:
# - https://requests.readthedocs.io/en/latest/

# Importamos los módulos necesarios
import requests

# Hacemos una petición HTTP a una URL
url = "https://www.marca.com"
page = requests.get(url)

# Mostramos el contenido de la respuesta
print(page.text)