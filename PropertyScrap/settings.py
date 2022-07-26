import os
from shutil import which
#selenium implementation 
SELENIUM_DRIVER_NAME = 'chrome'
SELENIUM_DRIVER_EXECUTABLE_PATH = which('chromedriver')
SELENIUM_DRIVER_ARGUMENTS=['--headless']  
DOWNLOADER_MIDDLEWARES = {
            'PropertyScrap.middlewares.SeleniumMiddleware': 543,
}

#pipelines
ITEM_PIPELINES = {
    "PropertyScrap.pipelines.PropertyScrapPipeline": 300,
}

#database settings
DATABASE = {
    "drivername": "postgres",
    "url": os.environ.get("POSTGRES_URL"),
    "host": os.environ.get("POSTGRES_HOST"),
    "port": os.environ.get("POSTGRES_PORT"),
    "username": os.environ.get("POSTGRES_USER"),
    "password": os.environ.get("POSTGRES_PASS"),
    "database": os.environ.get("POSTGRES_DB"),
}

DATABASE_URL = os.environ.get("DATABASE_URL")

LOG_LEVEL = "INFO"


#not to overload
DOWNLOAD_TIMEOUT = 540
DOWNLOAD_DELAY = 5
DEPTH_LIMIT = 10
EXTENSIONS = {
    'scrapy.extensions.telnet.TelnetConsole': None,
    'scrapy.extensions.closespider.CloseSpider': 1
}     

BOT_NAME = 'PropertyScrap'

SPIDER_MODULES = ['PropertyScrap.spiders']
NEWSPIDER_MODULE = 'PropertyScrap.spiders'



# Obey robots.txt rules
ROBOTSTXT_OBEY = False

