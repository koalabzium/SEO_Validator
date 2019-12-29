from CrawlingAndValidating.Validator import Validator
import re


class HeadingValidator(Validator):
    def __init__(self, url, content, result):
        self.url = url
        self.result = result
        self.content = content

    def validate(self):
        self.check_h1()
        self.check_structure()

    def check_h1(self):
        h1 = self.content.find_all('h1')
        if len(h1) == 0:
            self.result.heading_missing.append(self.url)
        elif len(h1) > 1:
            self.result.heading_too_many[self.url] = h1

    def check_structure(self):
        headings = self.content.find_all(re.compile('^h[1-6]$'))
        level = 1
        for i in headings:
            if level < int(i.name[1]):
                self.result.heading_structure.append(self.url)
                break
            level = int(i.name[1]) + 1
