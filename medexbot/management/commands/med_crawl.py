from django.core.management.base import BaseCommand

from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

from medexbot.spiders.med_parser import MedSpider


class Command(BaseCommand):
    help = "Release the Meds"

    def handle(self, *args, **options):
        process = CrawlerProcess(get_project_settings())
        process.crawl(MedSpider)
        process.start()
