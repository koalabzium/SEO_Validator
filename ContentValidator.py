from CrawlingAndValidating.Validator import Validator


class ContentValidator(Validator):
    def __init__(self, url, content, result):
        self.url = url
        self.result = result
        self.content = content

    def validate(self):
        self.check_links()
        self.check_content_length()

    def check_content_length(self):
        length = len(self.content.get_text())
        if length < 1500:
            self.result.little_content[self.url] = length

    def check_urls_amount(self, inbound, outbound):
        if inbound >= 8:
            self.result.inbound_counter[self.url] = inbound
        if outbound > 3:
            self.result.outbound_counter[self.url] = outbound
        if inbound + outbound >= 10:
            self.result.url_counter[self.url] = inbound + outbound

    def check_links(self):
        outbound_counter = 0
        inbound_counter = 0

        links = self.content.find_all('a')
        for l in links:
            if l.get('href').startswith('/') or not l.get('href').startswith('http'):
                inbound_counter += 1
            elif l.get('href').split('/')[2] == self.url.split('/')[2]:
                inbound_counter += 1
            else:
                outbound_counter += 1
            if l.get('title') is None:
                self.result.urls_missing_title.append(l.get('href'))

        self.check_urls_amount(inbound_counter, outbound_counter)
