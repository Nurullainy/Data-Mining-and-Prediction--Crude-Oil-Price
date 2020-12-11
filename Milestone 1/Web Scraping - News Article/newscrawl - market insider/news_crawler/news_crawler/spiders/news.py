# -*- coding: utf-8 -*-

import scrapy
from news_crawler.items import NewsItem
from scrapy.loader import ItemLoader

#To start a new scrapy project, use anaconda prompt, go to the desired folder or location, type 'scrapy startproject projectname'
#It will then create a default folder structure and files required.
#tutorial from http://mroseman.com/scraping-dynamic-pages/ and also https://www.youtube.com/watch?v=Wp6LRijW9wg
#Make sure chrome driver is downloaded
#Chrome driver version is based on the browser, update the google chrom browser to version 77 (latest as of 22 Sep 2019)
#Download chrome driver for version 77.Put the chromedriver.exe in the directory of the project folder.

            
class newsSpider(scrapy.Spider):
    name = 'newsinsider'
        
    def start_requests(self):
        for i in range(1,501):
            yield scrapy.Request('https://markets.businessinsider.com/news/ressort/commodities?p=%s' % i, callback=self.parse)
            
    def parse(self, response):
        for row in response.xpath("//table[@class='table table-small'][1]/tbody/tr"):
            l = ItemLoader(item=NewsItem(), selector = row)
            l.add_xpath('DateTime','td[1]')
            l.add_xpath("news_headline", 'td[2]/a/text()')
                        
            yield l.load_item()
        
      
            
