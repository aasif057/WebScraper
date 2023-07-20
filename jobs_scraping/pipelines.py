# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import mysql.connector
import os
passwd = os.environ['AZUREDB']
ssl_cert = os.environ['AZUREDBSSL'] 
# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import time

class JobsScrapingPipeline:
    def __init__(self):
        self.create_connection()
        self.create_table()
    def create_connection(self):
        self.cnx = mysql.connector.connect(user="aasif057", password=passwd, host="aasif-mysql.mysql.database.azure.com", port=3306, database="scraping", ssl_ca=ssl_cert, ssl_disabled=False)
        self.cursor = self.cnx.cursor()
    def create_table(self):
        self.cursor.execute("""DROP TABLE IF EXISTS jobs""")
        self.cursor.execute("""create table jobs(
                            job_title text, 
                            company_name text,
                            salary text,
                            experience text,
                            location text,
                            skills text,
                            url varchar(255) primary key)  
                            """  
        )
    
    def process_item(self, item, spider):
        self.store_db(item)
        return item
    def close_spider(self, spider):
        ## Close cursor & connection to database 
        self.cursor.close()
        self.cnx.close()
    def store_db(self,item):
        self.cursor.execute("""insert into jobs values (%s,%s,%s,%s,%s,%s,%s)""", (
                item['title'],
                item['company_name'],
                item['salary'],
                item['experience'],
                item['location'],
                item['skills'],
                item['url']
            )
            )
        self.cnx.commit()
    