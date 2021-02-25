#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 25 12:01:44 2021

@author: mutt
"""

from scrapy import cmdline
from enum import Enum , unique


@unique
class url_spy(Enum):
    vbiquge = "vbiquge_spy"
    
    
    
txt_url = "www.vbiquge.com/20_20331/"   #爬取书主目录





#setting
_have_log  = True  #true 输出scrapylog   false 不输出log

cmdline_order = "scrapy crawl "

if "vbiquge" in txt_url:
    cmdline_order = cmdline_order + url_spy.vbiquge.value
elif "qidian" in txt_url :
    print("qidian")
else:
    print("缺少当前网站爬虫")
    
    

if not _have_log :
    cmdline_order = cmdline_order + " --nolog"
    
cmdline_order = cmdline_order #+ " -a category=" + txt_url

print("运行参数", cmdline_order)
cmdline.execute(cmdline_order.split())
    
    
    
    
    
#cmdline.execute('scrapy crawl biquge_spy --nolog -a category=electronics'.split())    #带日志输出

#cmdline.execute('scrapy crawl biquge_spy'.split())            #不带日志输出





