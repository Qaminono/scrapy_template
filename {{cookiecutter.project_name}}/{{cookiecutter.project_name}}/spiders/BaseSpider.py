from abc import ABC

import scrapy
from ..items import MyAoItem
from bs4 import BeautifulSoup


class BaseSpider(scrapy.Spider, ABC):
    name = 'BaseSpider'

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.item = MyAoItem()

    def return_result(self, presentation):
        for row in presentation:
            session_name = row.get('session_name', row.get('title', ''))
            title = row.get('title', row.get('session_name', '')) if row.get('role', '') != 'Moderator' else ''
            url = row.get('url', '') if row.get('role', '') != 'Moderator' else ''
            self.item['name'] = row.get('name')
            self.item['affiliations'] = row.get('affiliations', '')
            self.item['role'] = row.get('role', '')
            self.item['email'] = row.get('email', '')
            self.item['session_name'] = session_name
            self.item['description'] = row.get('session_description', '')
            self.item['title'] = title
            self.item['abstract'] = row.get('abstract', '')
            self.item['url'] = url
            self.item['video_url'] = row.get('video_url', '')
            yield self.item

    @staticmethod
    def get_text(html):
        return BeautifulSoup(html, 'html.parser').text
