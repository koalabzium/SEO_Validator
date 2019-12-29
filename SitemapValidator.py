import requests
from CrawlingAndValidating.Validator import Validator


class SitemapValidator(Validator):
    def __init__(self, url, result):
        self.url = url
        self.result = result

    def validate(self):
        sitemap = self.url + "/sitemap.xml"
        response = requests.get(sitemap)
        if response.status_code == 404:
            self.result.missing_sitemap = True
