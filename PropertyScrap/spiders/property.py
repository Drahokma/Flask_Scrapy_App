import time
import scrapy
from scrapy import Selector
from scrapy.http import Request
from selenium import webdriver
from time import sleep
from selenium.common.exceptions import NoSuchElementException
from selenium import webdriver
from scrapy.http import TextResponse
from selenium.webdriver.common.keys import Keys
from PropertyScrap.items import PropertyscrapItem
#from ..items import PropertyscrapItem
import json
    
class PropertySpider(scrapy.Spider):
    name = 'property'
    allowed_domains = ['sreality.cz']  
        

    def start_requests(self):
        self.property_count = 0
        options = webdriver.ChromeOptions()
        options.add_argument("--disable-extensions")
        options.add_argument("--headless")
        options.add_argument("--disable-gpu")
        options.add_argument("--no-sandbox")
        self.property_count = 0
        self.driver = webdriver.Chrome(chrome_options=options, executable_path='/usr/local/bin/chromedriver')
        self.driver.implicitly_wait(10)  
        page = 0       
         
        while self.property_count <= 500:   
            page = page + 1       
            self.url = 'https://www.sreality.cz/hledani/prodej/byty?strana='+str(page)   
            self.driver.get(self.url)        
            # puts selenium response back into a scrapy response so we can use response.xpath and response.css
            print('crawling [' + self.url + '], hang tight...')
            yield scrapy.Request(self.url, callback=self.parse)                   
                   
        self.driver.quit()
            

    def parse(self, response):         
        properties = response.xpath("//div[@class='property ng-scope']")
   
        # scrape property in properties list
        for property in properties:
            # xpath of property name 
            property_URL = property.css('a').attrib['href']  
            property_name = property.css('span.name.ng-binding::text').get()
            property_locality = property.css('span.locality.ng-binding::text').get()
            self.property_count = self.property_count + 1
            if self.property_count <= 500:
                property_item = PropertyscrapItem()
                property_item['url'] = property_URL
                property_item['name'] = property_name
                property_item['locality'] = property_locality
                yield property_item
            #return property_item              

        