import bs4 as bs
from CrawlingAndValidating import ValidationResult
import re
import requests
from CrawlingAndValidating.Result import Result


class ValidatorOld(object):

    def __init__(self):
        self.result= Result()

    def title_validation(self, content, url):
        title = content.find('title')
        if title:
            if title.getText() in self.result.instance.repeated_titles:
                self.result.instance.repeated_titles[title.getText()].add(url)
            else:
                self.result.instance.repeated_titles[title.getText()] = set()
                self.result.instance.repeated_titles[title.getText()].add(url)
            if len(title.getText()) > 60 or len(title.getText()) < 50:
                self.result.instance.titles_wrong_size.append(url)
            for i in title.getText():
                if i in (",", "'", "\""):
                    self.result.instance.title_wrong_chars.append(url)
                    break
        else:
            self.result.instance.page_missing_title.append(url)

    def description_validation(self, content, url):
        description = None
        for i in content.find_all('meta'):
            if i.get('name') == "description":
                description = i.get('content')
                break

        if description is None:
            self.result.instance.description_missing.append(url)
        else:
            if description in self.result.instance.repeated_descriptions:
                self.result.instance.repeated_descriptions[description].add(url)
            else:
                self.result.instance.repeated_descriptions[description] = set()
                self.result.instance.repeated_descriptions[description].add(url)
            if len(description) > 160 or len(description) < 150:
                self.result.instance.description_wrong_size.append(url)

    def heading_validation(self, content, url):
        h1 = content.find_all('h1')
        if len(h1) == 0:
            self.result.instance.heading_missing.append(url)
        elif len(h1) > 1:
            self.result.instance.heading_too_many[url] = h1

        headings = content.find_all(re.compile('^h[1-6]$'))
        level = 1
        for i in headings:
            if level < int(i.name[1]):
                self.result.instance.heading_structure.append(url)
                break
            level = int(i.name[1]) + 1

    def content_length(self, content, url):
        length = len(content.get_text())
        if length < 1500:
            self.result.instance.little_content[url] = length

    def alt_text(self, content, url):
        for i in content.find_all('img'):
            if i.get('alt') is None or len(i.get('alt')) == 0:
                if url in self.result.instance.alt_text_missing:
                    self.result.instance.alt_text_missing[url] += 1
                else:
                    self.result.instance.alt_text_missing[url] = 1

    def open_graph(self, content, url):
        open_graph = False
        og_title = False
        og_image = False
        og_type = False
        og_url = False
        for i in content.find_all('meta'):
            if re.match('og:title', str(i.get('property'))):
                og_title = True
            elif re.match('og:url', str(i.get('property'))):
                og_url = True
            elif re.match('og:image', str(i.get('property'))):
                og_image = True
            elif re.match('og:type', str(i.get('property'))):
                og_type = True
        if og_image and og_title and og_type and og_url:
            open_graph = True
        if not open_graph:
            self.result.instance.no_open_graph.append(url)

    def validate(self, response_text, url):
        content = bs.BeautifulSoup(response_text, 'html5lib')
        self.title_validation(content, url)
        self.description_validation(content, url)
        self.heading_validation(content, url)
        self.content_length(content, url)
        self.alt_text(content, url)
        self.open_graph(content, url)
