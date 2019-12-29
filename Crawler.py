import requests
import bs4 as bs
import re
import json
from CrawlingAndValidating import URLResult, ValidatorOld
from CrawlingAndValidating.ValidationFacade import ValidationFacade
from CrawlingAndValidating.Result import Result


def create_starting_url(starting_url):
    if not starting_url.startswith('http'):
        return "http://"
    return starting_url


class Crawler(object):
    def __init__(self, starting_url, level):
        self.result = Result()
        self.starting_url = create_starting_url(starting_url)
        self.visited = set()
        self.max_level = level
        self.validatorOld = ValidatorOld.ValidatorOld()

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
        url = response.url
        self.visited.add(url)
        if not self.proper_status_code(response.status_code, prev, url):
            return
        content = bs.BeautifulSoup(response.text, 'html5lib')
        validator = ValidationFacade(content, url, self.starting_url, self.result)
        validator.validate()

        # self.validatorOld.validate(response.text, url)

        links = content.find_all('a')
        for l in links:
            child_url = self.create_child_url(l.get('href'))
            if child_url and child_url not in self.visited and level < self.max_level:
                self.crawl(child_url, level + 1, url)

    def start(self):
        self.crawl(self.starting_url, 0, "")
        self.check_robots()
        self.check_sitemap()
        # self.check_speed()
        # return self.result.create_result()

    def check_robots(self):
        robots = self.starting_url + "/robots.txt"
        response = requests.get(robots)
        if response.status_code == 404:
            self.validatorOld.result.missing_robots = True

    def check_sitemap(self):
        sitemap = self.starting_url + "/sitemap.xml"
        response = requests.get(sitemap)
        if response.status_code == 404:
            self.validatorOld.result.missing_sitemap = True

    def check_speed(self):
        x = "https://www.googleapis.com/pagespeedonline/v5/runPagespeed?url=" + str(self.starting_url)
        r = requests.get(x)
        final = r.json()
        try:
            time_to_first_byte = final['lighthouseResult']['audits']['time-to-first-byte']['numericValue']
            fct = final['lighthouseResult']['audits']['first-contentful-paint']['numericValue']
            self.validatorOld.result.time_to_first_byte = time_to_first_byte
            self.validatorOld.result.fct = fct
        except KeyError:
            print("Unable to get site speed")


if __name__ == "__main__":
    quotes = "http://quotes.toscrape.com/"
    moja = "http://koalabzium.github.io/test_page/"
    github = "https://github.com/koalabzium"
    line = "https://www.viviclabs.com/"
    # irenki = "https://healthyomnomnom.shoplo.com/producent/healthy-omnomnom" ---- nie działa, ogarnij kiedyśtam why
    # response = requests.get(moja)
    # print(response.url)
    # content = bs.BeautifulSoup(response.text, 'html5lib')

    crawler = Crawler(moja, 0)
    crawler.start()
