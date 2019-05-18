# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import mysql.connector


class ShopandmallscPipeline(object):
    def __init__(self):
        self.create_connection()

    def create_connection(self):
        self.conn = mysql.connector.connect(
            host='localhost',
            user='root',
            passwd='root',
            database='malls'
        )
   self.curr = self.conn.cursor()

    def insert_data(self, item):
        self.curr.execute(''' DELETE FROM sam_malls WHERE date = %s and
                              name = %s and
                              gla = %s and
                              city = %s and
                              url = %s''', (
            item['date'],
            item['name'],
            item['gla'],
            item['city'],
            item['url']
        ))    
        self.curr.execute(''' INSERT INTO sam_malls values (%s, %s, %s, %s, %s)''', (
            item['date'],
            item['name'],
            item['gla'],
            item['city'],
            item['url']
        ))
        self.conn.commit()

    def process_item(self, item, spider):
        self.insert_data(item)
        return item
