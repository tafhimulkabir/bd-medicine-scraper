import logging
import re

import scrapy
from django.db import IntegrityError

from crawler.models import Generic
from medexbot.items import DrugClassItem


class DrugClassSpider(scrapy.Spider):
    name = "drug_class"
    allowed_domains = ['medex.com.bd']
    start_urls = ['https://medex.com.bd/drug-classes']

    def parse(self, response):
        for drug_class in response.css('li.sc-2-list-item'):
            drug_class_link = drug_class.css('a ::attr("href") ').get()
            drug_class_id = re.findall("drug-classes/(\S*)/", drug_class_link)[0]
            drug_class_name = drug_class.css('a ::text').get()

            yield from response.follow_all(drug_class.css('a ::attr("href") '), self.parse_drug_generic,
                                           meta={"drug_class_id": drug_class_id, "drug_class_name": drug_class_name})

    def parse_drug_generic(self, response):
        item = DrugClassItem()
        item['drug_class_id'] = response.request.meta['drug_class_id']
        item['drug_class_name'] = response.request.meta['drug_class_name']
        item['generics_count'] = len(response.css('a.hoverable-block'))

        # todo generic ids mapping
        # generic_links = response.css('a.hoverable-block  ::attr(href)').extract()
        # generic_ids = [re.findall("generics/(\S*)/", generic_link)[0] for generic_link in generic_links]
        # for generic_id in generic_ids:
        #     try:
        #         generic = Generic.objects.get(generic_id=generic_id)
        #     except Generic.DoesNotExist as ge:
        #         logging.info(ge)
        #         generic = None
        #     except IntegrityError as ie:
        #         logging.info(ie)
        #         generic = None

        yield item
