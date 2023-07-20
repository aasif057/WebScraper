# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class JobsScrapingItem(scrapy.Item):
    # define the fields for your item here like:
    jobId = scrapy.Field()
    title = scrapy.Field()
    company_name = scrapy.Field()
    salary = scrapy.Field()
    experience = scrapy.Field()
    location = scrapy.Field()
    skills = scrapy.Field()
    url = scrapy.Field()

    
