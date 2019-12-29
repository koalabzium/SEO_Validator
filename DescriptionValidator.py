from CrawlingAndValidating.Validator import Validator


class DescriptionValidator(Validator):
    def __init__(self, url, content, result):
        self.url = url
        self.result = result
        self.content = content
        self.description = self.extract_description()

    def validate(self):
        if self.description is None:
            self.result.description_missing.append(self.url)
        else:
            self.check_if_repeated()
            self.check_length()

    def extract_description(self):
        for i in self.content.find_all('meta'):
            if i.get('name') == "description":
                return i.get('content')
        return None

    def check_if_repeated(self):
        if self.description in self.result.repeated_descriptions:
            self.result.repeated_descriptions[self.description].add(self.url)
        else:
            self.result.repeated_descriptions[self.description] = set()
            self.result.repeated_descriptions[self.description].add(self.url)

    def check_length(self):
        if len(self.description) > 160 or len(self.description) < 150:
            self.result.description_wrong_size.append(self.url)
