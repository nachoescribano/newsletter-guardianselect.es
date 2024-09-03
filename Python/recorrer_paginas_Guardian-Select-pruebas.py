import requests
from bs4 import BeautifulSoup

# Función para extraer noticias de una página web
def extraer_noticias(url, output_file):
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Aquí se asume que el titular está en <h2> y la fecha en <time> o un <span class="date">
        noticias = soup.find_all('article')  # Suposición: titulares y fechas están dentro de <article>
        
        if not noticias:
            output_file.write(f"No se encontraron noticias en {url}.\n")
        
        for noticia in noticias:
            titular = noticia.find('h2')
            fecha = noticia.find('time') or noticia.find('span', class_='date')
            
            if titular:
                titulo_text = titular.get_text(strip=True)
            else:
                titulo_text = "Titular no encontrado"

            if fecha:
                fecha_text = fecha.get_text(strip=True)
            else:
                fecha_text = "Fecha no disponible"
            
            output_file.write(f"{fecha_text} - {titulo_text}\n")
    
    except requests.exceptions.HTTPError as err:
        output_file.write(f"Error HTTP en {url}: {err}\n")
    except requests.exceptions.ConnectionError as err:
        output_file.write(f"Error de conexión en {url}: {err}\n")
    except requests.exceptions.Timeout as err:
        output_file.write(f"Tiempo de espera agotado en {url}: {err}\n")
    except Exception as e:
        output_file.write(f"Error en {url}: {e}\n")

# Lista de URLs de las empresas
urls_empresas = [
    "https://www.astiglass.com/noticias/",
    "http://www.controlglass.com/actualidad/",
    "https://cristaleriatama.com/es/noticias/",
    # Añade más URLs aquí
]

# Función para recorrer todas las URLs y extraer noticias
def recorrer_paginas():
    with open("resultados.txt", "w") as output_file:
        for url in urls_empresas:
            output_file.write(f"Extrayendo noticias de: {url}\n")
            extraer_noticias(url, output_file)
            output_file.write("-" * 50 + "\n")

recorrer_paginas()
