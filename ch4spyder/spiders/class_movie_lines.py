from scrapy.spiders import Spider
from scrapy import Request
from scrapy.loader import ItemLoader

from ch4spyder.items import Ch4SpyderItem


class movie_lines(Spider):
    name = "movie_lines"
    current_page = 1

    def start_requests(self):
        start_url = "https://www.mingyantong.com/allarticle/jingdiantaici"

        yield Request(start_url, callback=self.parse, errback=None)

        
    def parse(self, response, **kwargs):
        list_selector = response.xpath("//div[@class='wridesccon']")
        for one_selector in list_selector:
            movie = ItemLoader(item=Ch4SpyderItem(), selector=one_selector)
            movie.add_xpath("name", "div[2]/a/span/text()")
            movie.add_xpath("count", "div[2]/text()")
            movie.add_xpath("content", "div[1]/text()")
            movie.add_xpath("link", "div[2]/a/@href")

            yield movie.load_item()

        self.current_page += 1
        if self.current_page <= 5:
            next_url = "https://www.mingyantong.com/allarticle/jingdiantaici?page=%d" % self.current_page
            yield Request(next_url, callback=self.parse)
