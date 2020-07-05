# -*- coding: utf-8 -*-
import scrapy
from maoyan1.items import  Maoyan1Item
from scrapy.selector import Selector

class Maoyan2Spider(scrapy.Spider):
    name = 'maoyan2'
    allowed_domains = ['maoyao.com']
    start_urls = ['https://maoyan.com/board/4']

    def start_requests(self):
        for i in range(0, 10):
            url = f'https://maoyan.com/board/4?offset={i*10}'
            yield scrapy.Request(url=url, callback=self.parse, dont_filter=False)


    def parse(self, response):
        print(response.url)
        movies = Selector(response=response).xpath('//*[@id="app"]/div/div/div[1]/dl')
        for movie in movies:
            title = movie.xpath('./a/@title')
            link = movie.xpath('./a/@href')
            print('-----------')
            print(title)
            print(link)
            print('-----------')
            print(title.extract())
            print(link.extract())
            print(title.extract_first())
            print(link.extract_first())
            print(title.extract_first().strip())
            print(link.extract_first().strip())