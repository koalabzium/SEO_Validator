from CrawlingAndValidating.Validator import Validator
import re


class OpenGraphValidator(Validator):
    def __init__(self, url, content, result):
        self.url = url
        self.result = result
        self.content = content

    def validate(self):
        open_graph = False
        og_title = False
        og_image = False
        og_type = False
        og_url = False
        for i in self.content.find_all('meta'):
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
            self.result.no_open_graph.append(self.url)
