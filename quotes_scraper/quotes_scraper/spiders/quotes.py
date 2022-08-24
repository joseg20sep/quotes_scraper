from email.quoprimime import quote
from pickle import TRUE
from turtle import title

import scrapy
#titulo = response.xpath('//div/h1/a/text()').get()
#top_tag = response.xpath('//div[contains(@class,"tags-box")]//span[@class="tag-item"]/a/text()').getall()
#citas= response.xpath('//span[@class="text" and @itemprop="text"]/text()').getall()
#guardar los archivos en el formato deseado--> scrapy crawl quotes -o quotes.csv
#button --> response.xpath('//ul[@class = "pager"]//li[@class="next"]/a/@href').get()
# guardar solo el top que quieras --> scrapy crawl quotes -a top=5
class QuotesSpider(scrapy.Spider):
      # name es el nombre unico con el scrapy se va referir al spider dentro del proyect.
    # name debe ser unico.
    name = 'quotes'
     # Defiimos una lista de url a las cuales les vamos a realizar las peticiones http.
    start_urls = ['http://quotes.toscrape.com/']
    #custom_setting = {
    #    'FEED_URI': 'quotes.json',
    #    'FEED_FORMAT': 'json'
    #}
    custom_settings = {
        'FEED_URI': 'quotes.json',
        #Aqui eliges el formato en que se quiere guardar el archivo
        'FEED_FORMAT': 'json',
        'FEED_EXPORT_ENCODING': 'utf-8',
        'CONCURRENT_REQUESTS': 24,
        'MEMUSAGE_LIMIT_MB': 2048,
        'MEMUSAGE_NOTIFY_MAIL': ['joseg20sep@gmail.com'],
        'ROBOTSTXT_OBEY': True,
        'USER_AGENT': 'Joseg20sep'
    }
    def parse_only_quotes(self, response, **kwargs):
        if kwargs:
            quotes = kwargs['quotes']
        quotes.extend(response.xpath('//span[@class="text" and @itemprop="text"]/text()').getall())

        next_page_button_link = response.xpath(
            '//ul[@class = "pager"]//li[@class="next"]/a/@href').get()
        if next_page_button_link:
            yield response.follow(next_page_button_link, callback=self.parse_only_quotes, cb_kwargs={'quotes': quotes})
        else:
            yield{
                'quotes': quotes
            }

      # definir el metodo parse el cual nos sirve para analizar un archivo y extraer informacion valiosa a partir de el.
    def parse(self, response):
        #print('*'*10)
        #print('\n\n')
        title = response.xpath('//h1/a/text()').get()
        #print(f'Titulo: {title}')
        #print('\n\n')
        #print(response.status, response.headers)
        quotes = response.xpath('//span[@class="text" and @itemprop="text"]/text()').getall()
        #print('Citas: ')
        #for quotes in quotes:
        #    print(f'- {quotes}')
        #print('\n\n')
        top_tag = response.xpath('//div[contains(@class,"tags-box")]//span[@class="tag-item"]/a/text()').getall()
        top = getattr(self, 'top', None)
        if top:
            top = int(top)
            top_tag = top_tag[:top]
       #print('Top ten tag: ')
       #for tag in top_tag:
       #    print(f'- {tag}')
        #print('\n\n')
        #print('\n\n')
        #print('*' * 10)
        yield {
            'title': title,
            'top_tag': top_tag
        }
        next_page_button_link = response.xpath('//ul[@class = "pager"]//li[@class="next"]/a/@href').get()
        if next_page_button_link:
            yield response.follow(next_page_button_link, callback=self.parse_only_quotes, cb_kwargs={'quotes': quotes})
