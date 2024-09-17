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
def extraer_noticias_sector(url):
    headers = {
        'User-Agent': random.choice(user_agents)  # Rotar User-Agents
    }
    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Aquí puedes ajustar los selectores según la estructura del sitio web
        titulares = soup.find_all(['h2','h4'])  # Busca en <h2>, <h3>, y <h4>
        
        if not titulares:
            print(f"No se encontraron noticias en {url}.")
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

# Lista de URLs de sitios de noticias del sector
urls_sector = [
    "https://www.glassonweb.com/news",
    "https://www.glassonline.com/news/",
    "https://www.glass-international.com/news",
    "https://www.constructionnews.co.uk/",
    "https://europeanconstructionindustryfederation.eu/news",
    "https://www.glassmagazine.com/news",
    "https://www.vidrioperfil.com/es-es/buscador?query=guardian+select", 
    "https://www.infoconstruccion.es/noticias/construccion",
    "https://www.prefieres.es/category/noticias/", 
    "https://www.prefieres.es/?s=GUARDIAN+SELECT",
    # interempresas
    "https://www.interempresas.net/Buscador/?q=Guardian&oo=%F2%F3&CAC=R",
    "https://www.interempresas.net/Cerramientos_y_ventanas/Articulos/",
    "https://www.interempresas.net/Vidrio-plano/Articulos/",
    "https://www.interempresas.net/Vidrio-plano/FeriaVirtual/Noticias-Guardian-Glass-Express-S-L-197572.html",

    # Vidrioperfil.com
    "https://www.vidrioperfil.com/es-es/buscador?query=Guardian",
    
    # Glasstec
    "https://www.glasstec-online.com/en/Visitors/Hot_Topics/Overview_Hot_Topics"
    # Añade más URLs aquí
]

# Función para recorrer todas las URLs y extraer noticias del sector
def recorrer_paginas_sector():
    for url in urls_sector:
        print(f"Extrayendo noticias de: {url}")
        extraer_noticias_sector(url)
        print("-" * 50)
        time.sleep(random.uniform(1, 3))  # Añadir un retraso aleatorio entre 1 y 3 segundos

# Ejecuta la función directamente sin programar
recorrer_paginas_sector()
