# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

from scrapy_djangoitem import DjangoItem

from crawler.models import Medicine


class MedItem(DjangoItem):
    # define the fields for your item here like:
    django_model = Medicine


class GenericItem(DjangoItem):
    # define the fields for your item here like:
    django_model = Generic
