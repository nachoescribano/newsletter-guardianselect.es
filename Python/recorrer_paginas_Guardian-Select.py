import requests
from bs4 import BeautifulSoup
import time
import random

# Lista de diferentes User-Agents para rotar
user_agents = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.3 Safari/605.1.15',
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36',
    # Añade más User-Agents si es necesario
]

# Función para extraer noticias de una página web
def extraer_noticias(url):
    headers = {
        'User-Agent': random.choice(user_agents)  # Rotar User-Agents
    }
    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()  # Verifica que la solicitud fue exitosa
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Extraer titulares de noticias que están en etiquetas <h2>, <h3>, <h4>
        titulares = soup.find_all(['h2', 'h3', 'h4', 'h5'])  # Busca en <h2>, <h3>, <h4> y <h5>
        
        if not titulares:
            print("No se encontraron noticias en esta URL.")
        for titular in titulares:
            print(titular.get_text())
    
    except requests.exceptions.HTTPError as err:
        print(f"Error HTTP: {err}")
    except requests.exceptions.ConnectionError as err:
        print(f"Error de conexión: {err}")
    except requests.exceptions.Timeout as err:
        print(f"Tiempo de espera agotado: {err}")
    except Exception as e:
        print(f"Error: {e}")

# Lista de URLs de las empresas
urls_empresas = [
    "https://www.astiglass.com/noticias/",
    "http://www.controlglass.com/actualidad/",
    "https://www.crielec.com/novedades/",
    "https://www.dicrisur.es/blog",
    "http://www.k2glass.es/actualidad/",
    "https://serraglass.es/blog/",
    "http://www.viduplo.pt/es/Noticias",
    "https://vitralba.com/actualidad/",
    # Añade más URLs aquí
]

# Función para recorrer todas las URLs y extraer noticias
def recorrer_paginas():
    for url in urls_empresas:
        print(f"Extrayendo noticias de: {url}")
        extraer_noticias(url)
        print("-" * 50)
        time.sleep(random.uniform(1, 3))  # Añadir un retraso aleatorio entre 1 y 3 segundos

# Ejecuta la función directamente sin programar
recorrer_paginas()
