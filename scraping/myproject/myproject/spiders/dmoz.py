# -*- coding: utf-8 -*-
import scrapy


class DmozSpider(scrapy.Spider):
    name = "dmoz"
    allowed_domains = ["dmoztools.net"]
    start_urls = (
        'http://www.dmoztools.net/',
    )

    def parse(self, response):
        pass
