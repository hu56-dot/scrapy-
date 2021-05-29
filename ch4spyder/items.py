'''
Author: your name
Date: 2021-05-21 10:42:07
LastEditTime: 2021-05-28 13:10:35
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \PythonProjects\ch4spyder\ch4spyder\items.py
'''
# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html
import re

import scrapy
from scrapy.loader.processors import TakeFirst


# 进行基本的处理
def link_complete(link):
    link[0] = "https://www.mingyantong.com/" + link[0]
    return link


def count_delete(count):
    result = re.findall(".*\((.*)\).*", count[0])
    count_ = ''
    for x in result:
        count_ += x
    return int(count_)



class Ch4SpyderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name = scrapy.Field(output_processor=TakeFirst())
    link = scrapy.Field(input_processor=link_complete, output_processor=TakeFirst())
    # link = scrapy.Field(output_processor=TakeFirst())
    content = scrapy.Field(output_processor=TakeFirst())
    count = scrapy.Field(input_processor=count_delete, output_processor=TakeFirst())


