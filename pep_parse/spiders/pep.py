import re

import scrapy
from pep_parse.constants import NEXT_SIBLING, NUMBER_NAME, STATUS_XPATH
from pep_parse.items import PepParseItem

# from urllib.parse import urljoin


class PepSpider(scrapy.Spider):
    name = 'pep'
    allowed_domains = ['peps.python.org']
    start_urls = ['https://peps.python.org/']

    def parse_pep(self, response):
        title = response.css('h1.page-title::text').get().replace('"', '')
        number, name = re.search(NUMBER_NAME, title).groups()
        status = response.xpath(f'{STATUS_XPATH}{NEXT_SIBLING}').get()
        data = {
            'number': number,
            'name': name,
            'status': status,
        }
        yield PepParseItem(data)

    def parse(self, response):
        pep_list = response.css('section[id="numerical-index"]')
        pep_links = pep_list.css(
            'a[class="pep reference internal"]::attr(href)').getall()
        for pep_link in pep_links:
            yield response.follow(pep_link, callback=self.parse_pep)
