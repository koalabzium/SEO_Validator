from py_w3c.validators.html.validator import HTMLValidator
from CrawlingAndValidating.Validator import Validator

class W3CValidator(Validator):
    def __init__(self, url, result):
        self.url = url
        self.result = result

    def validate(self):
        vld = HTMLValidator()
        vld.validate(self.url)
        self.result.w3c = vld.errors
