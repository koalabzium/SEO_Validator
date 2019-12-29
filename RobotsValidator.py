import requests
from CrawlingAndValidating.Validator import Validator


class RobotsValidator(Validator):
    def __init__(self, url, result):
        self.url = url
        self.result = result

    def validate(self):
        robots = self.url + "/robots.txt"
        response = requests.get(robots)
        if response.status_code == 404:
            self.result.missing_robots = True
