import scrapy
import pprint as pprt



class VbiqugeSpySpider(scrapy.Spider):
    name = 'vbiquge_spy'
    allowed_domains = ['http://www.vbiquge.com/']
    start_urls = ['http://www.vbiquge.com//']

    def parse(self, response):
        
        print(response.url)
        
        pass
