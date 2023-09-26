# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import sqlite3


# class SpiderExamplePipeline:
#     def process_item(self, item, spider):
#         return item

class SQLitePipeline:
    
    def open_spider(self, spider):
        self.connection = sqlite3.connect('transcript.db')
        self.c = self.connection.cursor()

        try:
            self.c.execute('''
                           CREATE TABLE transcripts(
                           name TEXT,
                           plot TEXT
                             )
                          ''')
            
            # save changes
            self.connection.commit()
        except sqlite3.OperationalError:
            pass

    def close_spider(self, spider):
        self.connection.close()


    def process_item(self, item, spider):
        self.c.execute('''
                       INSERT INTO transcripts (name,plot) VALUES (?,?)
                        ''',
                        (
                        item.get('name'),
                        item.get('plot'),
                        )
                       )

        self.connection.commit()
        return item
