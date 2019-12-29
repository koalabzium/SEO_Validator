from CrawlingAndValidating.Result import Result
from CrawlingAndValidating.Validator import Validator


class URLValidator(Validator):

    def __init__(self, url, result):
        self.url = url
        self.result = result

    def validate(self):
        self.check_ssl()
        self.check_url_chars()

    def check_ssl(self):
        if not self.url.startswith('https'):
            self.result.http_urls.append(self.url)

    def check_url_chars(self):
        for i in self.url:
            if i == "_" or i == " " or i.isupper():
                self.result.urls_wrong_chars.append(self.url)
                break
