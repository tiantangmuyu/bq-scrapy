import scrapy
from biquge.items import BiqugeItem

zhangjie_list = []

class BiqugeSpySpider(scrapy.Spider):
    name = 'biquge_spy'
    allowed_domains = ['http://www.vbiquge.com']
    start_urls = ['http://www.vbiquge.com/20_20331/']
    
    

    def parse(self, response):
        
        
        
        
        title = scrapy.Selector(response).xpath('//*[@id="list"]/dl/dt/text()').extract()[0]
        zhangjie = scrapy.Selector(response).xpath('//*[@id="list"]/dl//dd/a/text()').extract()
        txt_url = scrapy.Selector(response).xpath('//*[@id="list"]/dl//dd/a/@href').extract()
        
        #print(title,zhangjie,txt_url)
        
        
        
        for zj,t_url in zip(zhangjie,txt_url):
            if zj not in zhangjie_list:
                
                zhangjie_list.append(zj)
                
                t_url = 'https://www.vbiquge.com' + t_url
                
                
                #item["zhengwen"] = t_url
                
                yield scrapy.Request(t_url,callback =self.pic_download,dont_filter = True)
                
        
    def pic_download(self,response):
        
        text = scrapy.Selector(response).xpath('//*[@id="content"]//text()').extract()
        
        textstr = "\n".join(text)
        
        textstr = textstr.replace(u'\xa0', u' ')
        
        zj = scrapy.Selector(response).xpath('//*[@class="bookname"]/h1/text()').extract()[0]
        
        
        item = BiqugeItem()
        
        item["zhangjie"] = zj
        
        item["zhengwen"] = textstr
        
        yield item
        
        
        
        
        
        pass
        
