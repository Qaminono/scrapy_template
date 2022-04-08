import scrapy
from .BaseSpider import BaseSpider


class {{ cookiecutter.spider_name.capitalize() }}Spider(BaseSpider):
    name = '{{ cookiecutter.spider_name }}'
    allowed_domains = ['{{ cookiecutter.scrapy_site }}']
    start_urls = ['http://{{ cookiecutter.scrapy_site }}']

    def parse(self, response):
        pass
