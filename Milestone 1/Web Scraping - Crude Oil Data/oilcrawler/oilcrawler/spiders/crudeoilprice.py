"""
Xpath
//div/a

//div/a/text()

//div/a/@href

//p[@id = 'xxx']

//p[@class = 'xxx']

"""

import scrapy
from datetime import date
from datetime import timedelta
from oilcrawler.items import OilItem
from scrapy.loader import ItemLoader


# To start a new scrapy project, use anaconda prompt, go to the desired folder or location, type 'scrapy startproject projectname'
# It will then create a default folder structure and files required.
# tutorial from http://mroseman.com/scraping-dynamic-pages/ and also https://www.youtube.com/watch?v=Wp6LRijW9wg
# Make sure chrome driver is downloaded
# Chrome driver version is based on the browser, update the google chrom browser to version 80 (latest as of 22 Sep 2019)
# Download chrome driver for version 80.Put the chromedriver.exe in the directory of the project folder.

class oilSpider(scrapy.Spider):
    name = 'oilpricespider'
    last20 = (date.today() - timedelta(days=7300)).strftime('%d.%m.%y')
    todayDate = date.today().strftime('%d.%m.%y')
    oil_url = 'https://sg.finance.yahoo.com/quote/CL%3DF/history?period1=953683200&period2=1584403200&interval=1d&filter=history&frequency=1d' \
             + last20 + '_' + todayDate
    start_urls = [oil_url]

    def parse(self, response):
        for data in response.xpath("//div[@class='Pb(10px) Ovx(a) W(100%)']/table/tbody/tr"):
            l = ItemLoader(item=OilItem(), selector=data)
            l.add_xpath("Date", 'td[1]//text()')
            l.add_xpath("Open_price", 'td[2]//text()')
            l.add_xpath("High_price", 'td[3]//text()')
            l.add_xpath("Low_price", 'td[4]//text()')
            l.add_xpath("Close_price", 'td[5]//text()')
            l.add_xpath("Adj_Close", 'td[6]//text()')
            l.add_xpath("Volume", 'td[7]//text()')

            yield l.load_item()