# Módulos
import requests
from bs4 import BeautifulSoup

#-------------------------------------------------------------------------------
# Funciones

def obtener_titulares(url, etiqueta, clase):
    # Hacemos una petición HTTP a una URL
    page = requests.get(url)

    # Convertimos la respuesta en un objeto BeautifulSoup
    soup = BeautifulSoup(page.content, "html.parser")

    # Obtenemos todos las etiquetas del documento
    titulares = soup.find_all(etiqueta, class_=clase)

    # Mostramos por pantalla los valores obtenidos
    count = 1
    for titular in titulares:
        print(f"{count}. {titular.text.strip()}")
        count = count + 1

#-------------------------------------------------------------------------------
# Programa Principal

lista_webs = [
    {'url':'https://www.lavozdealmeria.com', 'etiqueta': 'h2', 'clase': 'titular_portadilla1'},
    {'url':'https://www.lavozdealmeria.com', 'etiqueta': 'h2', 'clase': 'titular_portadilla2'},
    {'url':'https://www.diariodealmeria.es', 'etiqueta': 'h1', 'clase': 'headline'},
    {'url':'https://elpais.com', 'etiqueta': 'h2', 'clase': 'c_t'}
]

for web in lista_webs:
    obtener_titulares(web['url'], web['etiqueta'], web['clase'])