import requests
import bs4 as bs
from CrawlingAndValidating import URLResult, Validator


class Crawler(object):
    def __init__(self, starting_url, level):
        self.starting_url = starting_url
        self.visited = set()
        self.domain = starting_url.split('/')[2]
        self.max_level = level
        self.result = URLResult.URLResult()
        self.validator = Validator.Validator()

    def create_and_check_url(self, url):

        if url.startswith('/'):
            return self.starting_url + url
        if url.startswith('http'):
            if not url.startswith('https'):
                self.result.http_urls.append(url)
            url_split = url.split('/')
            if url_split[2] == self.domain:
                return url
            else:
                return None
        else:
            return self.starting_url + '/' + url

    def check_urls_amount(self, inbound, outbound, url):
        if inbound >= 5:
            self.result.inbound_counter[url] = inbound
        if outbound > 3:
            self.result.outbound_counter[url] = outbound
        if inbound + outbound >= 8:
            self.result.url_counter[url] = inbound + outbound

    def proper_status_code(self, status_code, prev, url):
        if status_code not in (200, 301):
            if status_code == 302:
                if prev in self.result.urls_302:
                    self.result.urls_302[prev].append(url)
                else:
                    self.result.urls_302[prev] = []
                    self.result.urls_302[prev].append(url)
            else:
                if prev in self.result.broken_urls:
                    self.result.broken_urls[prev].append(url)
                else:
                    self.result.broken_urls[prev] = []
                    self.result.broken_urls[prev].append(url)
            return False
        return True

    def crawl(self, url, level, prev):

        inbound_counter = 0
        outbound_counter = 0

        response = requests.get(url)
        self.visited.add(url)

        if not self.proper_status_code(response.status_code, prev, url):
            return

        content = bs.BeautifulSoup(response.text, 'html5lib')
        self.validator.validate(response.text, url)

        links = content.find_all('a')
        # print("CRAWLING: " + str(url) + " with level " + str(level))
        for l in links:
            child_url = self.create_and_check_url(l.get('href'))
            if l.get('title') is None:
                self.result.urls_missing_title.append(l.get('href'))
            if not child_url:
                outbound_counter += 1
            else:
                for i in child_url:
                    if i == "_" or i == " " or i.isupper():
                        self.result.urls_wrong_chars.append(child_url)
                        break
                inbound_counter += 1
                if child_url not in self.visited and level < self.max_level:
                    self.crawl(child_url, level + 1, url)
        self.check_urls_amount(inbound_counter, outbound_counter, url)

    def start(self):
        self.crawl(self.starting_url, 0, "")


if __name__ == "__main__":
    quotes = "http://quotes.toscrape.com/"
    moja = "https://koalabzium.github.io/test_page/"
    github = "https://github.com/koalabzium"
    response = requests.get(moja)
    content = bs.BeautifulSoup(response.text, 'html5lib')
    print(content.find_all('h1'))
    # for i in content.find_all('meta'):
    #     if i.get('name') == "description":
    #         print(i.get("content"))
    # print()
    # links = content.find_all('a')
    # for l in links:
    #     child_url = l.get('title')
    #     print(child_url)

    # crawler = Crawler(moja, 1)
    # crawler.start()
    # crawler.result.show()
    # crawler.validator.result.show()