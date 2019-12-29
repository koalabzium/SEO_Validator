from CrawlingAndValidating.Validator import Validator


class TitleValidator(Validator):
    def __init__(self, url, content, result):
        self.url = url
        self.result = result
        self.content = content

        self.title = content.find('title')

    def validate(self):
        if self.title:
            self.check_if_repeated()
            self.check_length()
            self.check_title_chars()
        else:
            self.result.page_missing_title.append(self.url)

    def check_if_repeated(self):
        if self.title.getText() in self.result.repeated_titles:
            self.result.repeated_titles[self.title.getText()].add(self.url)
        else:
            self.result.repeated_titles[self.title.getText()] = set()
            self.result.repeated_titles[self.title.getText()].add(self.url)

    def check_length(self):
        if len(self.title.getText()) > 60 or len(self.title.getText()) < 50:
            self.result.titles_wrong_size.append(self.url)

    def check_title_chars(self):
        for i in self.title.getText():
            if i in (",", "'", "\""):
                self.result.title_wrong_chars.append(self.url)
                break
