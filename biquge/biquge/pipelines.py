# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter



class BiqugePipeline:
    def process_item(self, item, spider):
        
        
        zj = item["zhangjie"]
        t_url = item["zhengwen"]
        
        print("正在下载>>>", zj , "<<<正文>>>" , t_url)
        
        path = "/Users/mutt/Documents/GitHub/小说下载/" + zj
        
        with open(path,'w') as f:    #设置文件对象
            f.write(t_url)
            f.close()
    
        
        
        
        
        
        
        return item
