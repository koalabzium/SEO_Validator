from CrawlingAndValidating.Validator import Validator


class GraphicsValidator(Validator):
    def __init__(self, url, content, result):
        self.url = url
        self.result = result
        self.content = content

    def validate(self):
        self.check_alt_text()

    def check_alt_text(self):
        for i in self.content.find_all('img'):
            if i.get('alt') is None or len(i.get('alt')) == 0:
                if self.url in self.result.alt_text_missing:
                    self.result.alt_text_missing[self.url] += 1
                else:
                    self.result.alt_text_missing[self.url] = 1
