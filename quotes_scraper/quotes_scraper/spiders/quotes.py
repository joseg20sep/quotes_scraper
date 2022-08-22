from turtle import title
import scrapy
#titulo = response.xpath('//div/h1/a/text()').get()
#top_ten_tag = response.xpath('//div[contains(@class,"tags-box")]//span[@class="tag-item"]/a/text()').getall()
#citas= response.xpath('//span[@class="text" and @itemprop="text"]/text()').getall()
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
        title = response.xpath('//h1/a/text()').get()
        print(f'Titulo: {title}')
        print('\n\n')
        #print(response.status, response.headers)
        quotes = response.xpath('//span[@class="text" and @itemprop="text"]/text()').getall()
        print('Citas: ')
        for quotes in quotes:
            print(f'- {quotes}')
        print('\n\n')

        top_ten_tag = response.xpath('//div[contains(@class,"tags-box")]//span[@class="tag-item"]/a/text()').getall()
        print('Top ten tag: ')
        for tag in top_ten_tag:
            print(f'- {tag}')
        print('\n\n')

        print('\n\n')
        print('*' * 10)
