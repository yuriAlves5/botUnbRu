import scrapy
from scrapy.http import Request

class RuhtmlSpider(scrapy.Spider):
    name = 'ruhtml'
    
    def start_requests(self):
        urls = ['https://ru.unb.br/index.php/cardapio-refeitorio']
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        page = response.url.split("/")[-2]
        pdfs = 'a[href$=".pdf"]::attr(href)'
        for href in response.css(pdfs).extract():
            yield Request(
                url=response.urljoin(href),
                callback=self.save_pdf
            )
                
            

        filename = f'ruhtml-{page}.html'
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log(f'Saved file {filename}')

    def save_pdf(self, response):
        filename = response.url.split("/")[-1]
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log(f'Saved file {filename}')