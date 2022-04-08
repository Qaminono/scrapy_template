# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
from openpyxl import Workbook
import logging
from scrapy.exceptions import DropItem

# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

COLUMNS = ['Name (incl. titles)', 'Affiliation/Organisation and location', 'Role', 'Email', 'Session Name',
           'Session Description', 'Presentation Title', 'Presentation Abstract', 'Abstract URL', 'Video URL']


class XlsxPipeline:
    unique_list = list()

    def open_spider(self, spider):
        self.file_name = f'{spider.name.capitalize()}.xlsx'
        self.wb = Workbook()
        self.ws = self.wb.active
        self.ws.append(COLUMNS)
        logging.log(logging.INFO, 'Spider started')

    def process_item(self, item, spider):
        current_item = [item['name'], item['role'], item['session_name'], item['title']]
        # if current_item in self.unique_list:
        #     logging.log(logging.WARNING, 'Dropped because the item is already on the list')
        #     print('DROP\nDROP\nDROP\nDROP\nDROP')
        #     raise DropItem(item)
        # if not item['name']:
        #     logging.warning("Dropped because the item doesn't have person name")
        #     raise DropItem(item)
        self.ws.append(list(item.values()))
        self.unique_list.append(current_item)
        return item

    def close_spider(self, spider):
        logging.log(logging.INFO, 'Spider closed')
        self.wb.save(self.file_name)
        logging.log(logging.INFO, f'File was saved as {self.file_name}')
