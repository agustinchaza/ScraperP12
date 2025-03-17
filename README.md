# ScraperP12
ScraperP12 es un **web scraper** desarrollado con Scrapy para obtener información del sitio **Página 12**.  
Permite realizar búsquedas de artículos utilizando una palabra clave específica.

## Instalación y uso
### 1. Clonar el repositorio
En tu terminal, clona el repositorio donde está alojado el proyecto:


git clone <https://github.com/agustinchaza/ScraperP12>

Luego, accede al directorio del proyecto:
cd scrapperPagina12

### 2. Ejecutar el scraper
Para ejecutar el scraper, usa el siguiente comando:

scrapy crawl pagina12

Este comando buscará artículos relacionados con la palabra clave definida en el archivo config.json.

Los datos se obtendran en el archivo output.csv

### 3. Búsqueda personalizada
Si deseas buscar artículos sobre un tema específico, puedes pasar la palabra clave como argumento:


scrapy crawl pagina12 -a query="tu_palabra_clave"

Por ejemplo, para buscar artículos sobre educación:
scrapy crawl pagina12 -a query="educación"

### 4. Configuración
Si no se proporciona una palabra clave en la ejecución, el scraper usará la búsqueda por defecto definida en config.json:

{
  "default_search_query": "economia"
}

Puedes editar este archivo para cambiar la búsqueda predeterminada.

## Requisitos
### Python 3.x
### Scrapy instalado (pip install scrapy)
### Twisted==22.10.0 (pip install Twisted==22.10.0)