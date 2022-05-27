# Módulos necesarios:
# - requests
# - beautifulsoup
# - csv
#
# python3 -m pip install requests 
# python3 -m pip install beautifulsoup4

# Referencias:
# - https://requests.readthedocs.io/en/latest/
# - https://www.crummy.com/software/BeautifulSoup/bs4/doc/

# Importamos los módulos necesarios
import requests
from bs4 import BeautifulSoup
import csv

# Hacemos una petición HTTP a una URL
url = "https://www.marca.com"
page = requests.get(url)

# Mostramos el contenido de la respuesta
#print(page.text)

# Convertimos la respuesta en un objeto BeautifulSoup
soup = BeautifulSoup(page.content, "html.parser")

# Obtenemos todos las etiquetas h2 del documento
titulares = soup.find_all("h2")

# Mostramos la lista de etiquetas h2
#print(titulares)

# Mostramos el texto que hay dentro de cada etiqueta h2
# Utilizamos el método .strip() para eliminar los espacios en blanco al inicio y al final de la cadena
# Mostramos un número delante de cada titular

# Definimos el nombre del archivo .csv
filename = 'titulares.csv'

# Abrimos el archivo en modo escritura
with open(filename, 'w') as file:
    # Creamos el objeto writer que escibirá en el archivo csv
    writer = csv.writer(file)    

    # Escrimos la primera fila del archivo csv que será la cabecera
    writer.writerow(["Número", "Titular"])

    # Recorremos la lista de titulares y los escribimos en el archivo línea a línea
    count = 1
    for titular in titulares:
        # Escribimos una fila con un titular en el archivo
        writer.writerow([count, titular.text.strip()])
        count = count + 1
