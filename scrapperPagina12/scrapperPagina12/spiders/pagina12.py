import os
import random
import time

import scrapy
from scrapperPagina12.utilities.dateConversor import convertirFecha2Iso
from scrapperPagina12.utilities.lectorJSON import cargar_configuracion


# Clase principal del Spider para extraer artículos de la página "pagina12.com.ar"
class Pagina12Spider(scrapy.Spider):
    name = "pagina12"  # Nombre del Spider, utilizado por Scrapy
    allowed_domains = ["pagina12.com.ar"]  # Dominio permitido para la araña

    def __init__(self, search_query=None, *args, **kwargs):
        """
        Inicializa el Spider y configura los parámetros iniciales como la búsqueda por defecto.
        También maneja la eliminación del archivo 'output.csv' si existe.
        """
        # Eliminar archivo de salida si existe
        if os.path.exists('output.csv'):
            os.remove('output.csv')

        # Llamar al constructor de la clase base de Scrapy
        super(Pagina12Spider, self).__init__(*args, **kwargs)

        # Cargar la configuración desde un archivo JSON
        config = cargar_configuracion()

        # Definir la consulta de búsqueda, si no se pasa, usa el valor por defecto
        self.search_query = search_query or config.get("default_search_query", "economia")

        # Establecer la URL inicial para la búsqueda
        self.start_urls = [f"https://www.pagina12.com.ar/buscar?q={self.search_query}"]

    def parse(self, response):

        """
        Parsear la respuesta de la página de búsqueda para extraer los artículos y gestionar la paginación.
        """
        # Buscar todos los artículos en la página
        articles = response.xpath('//article[contains(@class, "article-item article-item--teaser")]')

        # Extraer el enlace a la siguiente página, si existe
        next_page = response.css("a.next::attr(href)").get()
        if next_page:
            next_page_url = response.urljoin(next_page)  # Crear URL completa para la siguiente página
            yield scrapy.Request(url=next_page_url, callback=self.parse)  # Realizar la solicitud a la siguiente página

        # Iterar sobre los artículos extraídos y parsearlos
        for article in articles:
            yield self.parse_article(article, response)

    def parse_article(self, article, response):
        """
        Extrae los datos específicos de cada artículo y devuelve un diccionario con los detalles.
        """
        # Extraer el título, URL, descripción, fecha, imagen y autor del artículo
        titulo = self.extract_text(article, './/h4/a/text()')
        url = self.get_full_url(article, response)
        descripcion = self.extract_text(article, './/p/a/text()')
        fecha = self.extract_text(article, './/div[contains(@class, "date")]/text()')
        imagen = self.extract_text(article, './/img/@src')
        autor = self.extract_autor(article)

        # Retornar los datos del artículo como un diccionario
        return {
            "titulo": titulo,
            "url": url,
            "descripcion": descripcion,
            "fecha": convertirFecha2Iso(fecha),  # Convertir la fecha a formato ISO
            "imagen": imagen,
            "autor": autor,
        }

    def extract_text(self, article, xpath_query, default=None):
        """
        Extrae el texto de un nodo utilizando la consulta XPath dada.
        Si no se encuentra el nodo, devuelve un valor por defecto (None o el valor proporcionado).
        """
        result = article.xpath(xpath_query).get()
        return result.strip() if result else default

    def get_full_url(self, article, response):
        """
        Obtiene la URL completa de un artículo a partir de su enlace relativo.
        """
        relative_url = article.xpath('.//h4/a/@href').get(default='')
        return response.urljoin(relative_url)  # Combina la URL base con la relativa

    def extract_autor(self, article, default=None):
        """
        Extrae el nombre del autor del artículo.
        Si no encuentra una fecha antes que un autor entonces no hay autor
        """
        result = article.xpath(
            './/div[contains(@class, "author")]//a/text() | .//div[contains(@class, "date")]/text()').get()

        # Verifica si el autor tiene un formato incorrecto o múltiple, y lo limpia
        if result and result.count(" de ") > 1:
            print(result)  # Para depurar
            result = " "  # Asignar un valor vacío si hay más de un "de" en el autor

        return result.strip() if result else default

    def closed(self, reason):
        """
        Se ejecuta cuando el Spider termina su ejecución. Aquí puedes agregar estadísticas o logs.
        """
        pass
        stats = self.crawler.stats.get_stats()
        print(stats)
