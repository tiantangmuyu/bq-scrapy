#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 25 12:01:44 2021

@author: mutt
"""

from scrapy import cmdline


#setting
txt_url = ""
_have_log  = False

if _have_log :
    cmdline.execute('scrapy crawl biquge_spy --nolog'.split())    #带日志输出
else:
    cmdline.execute('scrapy crawl biquge_spy'.split())            #不带日志输出
