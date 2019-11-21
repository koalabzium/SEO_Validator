import bs4 as bs
from CrawlingAndValidating import ValidationResult


class Validator(object):

    def __init__(self):
        self.result = ValidationResult.ValidationResult()

    def title_validation(self, content, url):
        title = content.find('title')
        if title:
            if title.getText() in self.result.repeated_titles:
                self.result.repeated_titles[title.getText()].add(url)
            else:
                self.result.repeated_titles[title.getText()] = set()
                self.result.repeated_titles[title.getText()].add(url)
            if len(title.getText()) > 60 or len(title.getText()) < 50:
                self.result.titles_wrong_size.append(url)
            for i in title.getText():
                if i in (",","'", "\""):
                    self.result.title_wrong_chars.append(url)
                    break
        else:
            self.result.page_missing_title.append(url)

    def description_validation(self, content, url):
        description = None
        for i in content.find_all('meta'):
            if i.get('name') == "description":
                description = i.get('content')
                break

        if description is None:
            self.result.description_missing.append(url)
        else:
            if description in self.result.repeated_descriptions:
                self.result.repeated_descriptions[description].add(url)
            else:
                self.result.repeated_descriptions[description] = set()
                self.result.repeated_descriptions[description].add(url)
            if len(description) > 160 or len(description) < 150:
                self.result.description_wrong_size.append(url)

    def heading_validation(self, content, url):
        h1 = content.find_all('h1')

        if len(h1) > 1:
            self.result.heading_too_many[url] = h1




    def validate(self, response_text, url):
        content = bs.BeautifulSoup(response_text, 'html5lib')
        self.title_validation(content, url)
        self.description_validation(content, url)
