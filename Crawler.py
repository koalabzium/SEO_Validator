import requests
import bs4 as bs
from CrawlingAndValidating.ValidationFacade import ValidationFacade
from CrawlingAndValidating.Result import Result


def create_starting_url(starting_url):
    if not starting_url.startswith('http'):
        return "http://"
    return starting_url


class Crawler(object):
    def __init__(self, starting_url, level, config):
        self.result = Result(starting_url, level, config)
        self.starting_url = create_starting_url(starting_url)
        self.visited = set()
        self.max_level = level
        self.config = config

    def create_child_url(self, url):
        if url.startswith('/'):
            return self.starting_url + url
        if url.startswith('http'):
            url_split = url.split('/')
            if url_split[2] == self.starting_url.split('/')[2]:
                return url
            else:
                return None
        else:
            return self.starting_url + '/' + url

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
        response = requests.get(url)
        if url == self.starting_url:
            self.starting_url = response.url
        url = response.url
        self.visited.add(url)
        if not self.proper_status_code(response.status_code, prev, url):
            return
        content = bs.BeautifulSoup(response.text, 'html5lib')
        validator = ValidationFacade(content, url, self.starting_url, self.result, self.config)
        validator.validate()

        links = content.find_all('a')
        for link in links:
            child_url = self.create_child_url(link.get('href'))
            if child_url and child_url not in self.visited and level < self.max_level:
                self.crawl(child_url, level + 1, url)

    def start(self):
        self.crawl(self.starting_url, 0, "")
        # print(self.result.create_report())

        # self.result.show()
        return self.result.create_report()

if __name__ == "__main__":
    quotes = "http://quotes.toscrape.com/"
    moja = "http://koalabzium.github.io/test_page/"
    github = "https://github.com/koalabzium"
    line = "https://www.viviclabs.com/"
    # irenki = "https://healthyomnomnom.shoplo.com/producent/healthy-omnomnom" ---- nie działa, ogarnij kiedyśtam why
    # response = requests.get(moja)
    # print(response.url)
    # content = bs.BeautifulSoup(response.text, 'html5lib')

    crawler = Crawler(moja, 1)
    crawler.start()
