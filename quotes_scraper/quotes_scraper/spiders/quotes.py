import scrapy

class QuotesSpider(scrapy.Spider):
      # name es el nombre unico con el scrapy se va referir al spider dentro del proyect.
    # name debe ser unico.
    name = 'quotes'
     # Defiimos una lista de url a las cuales les vamos a realizar las peticiones http.
    start_urls = ['http://quotes.toscrape.com/']
      # definir el metodo parse el cual nos sirve para analizar un archivo y extraer informacion valiosa a partir de el.

    def parse(self, response):
        print('*'*10)
        print('\n\n')
        print(response.status, response.headers)
        print('*'*10)
        print('\n\n')