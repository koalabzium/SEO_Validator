from CrawlingAndValidating.URLValidator import URLValidator
from CrawlingAndValidating.ContentValidator import ContentValidator
from CrawlingAndValidating.SpeedValidator import SpeedValidator
from CrawlingAndValidating.SitemapValidator import SitemapValidator
from CrawlingAndValidating.RobotsValidator import RobotsValidator
from CrawlingAndValidating.TitleValidator import TitleValidator
from CrawlingAndValidating.DescriptionValidator import DescriptionValidator
from CrawlingAndValidating.HeadingValidator import HeadingValidator
from CrawlingAndValidating.GraphicsValidator import GraphicsValidator
from CrawlingAndValidating.OpenGraphValidator import OpenGraphValidator
from CrawlingAndValidating.W3CValidator import W3CValidator


class ValidationFacade:

    def __init__(self, content, url, starting_url, result, config):
        self.config = config
        self.url_validator = URLValidator(url, result)
        self.content_validator = ContentValidator(url, content, result)
        self.speed_validator = SpeedValidator(starting_url, result)
        self.sitemap_validator = SitemapValidator(starting_url, result)
        self.robots_validator = RobotsValidator(starting_url, result)
        self.title_validator = TitleValidator(url, content, result)
        self.description_validator = DescriptionValidator(url, content, result)
        self.heading_validator = HeadingValidator(url, content, result)
        self.graphics_validator = GraphicsValidator(url, content, result)
        self.open_graph_validator = OpenGraphValidator(url, content, result)
        self.w3c_validator = W3CValidator(url, result)
        self.url = url
        self.staring_url = starting_url
        self.result = result

    def validate(self):
        self.url_validator.validate()
        self.content_validator.validate()
        self.title_validator.validate()
        self.description_validator.validate()
        self.heading_validator.validate()
        self.graphics_validator.validate()
        self.open_graph_validator.validate()
        if self.url == self.staring_url:
            if self.config['measure_speed']:
                self.speed_validator.validate()
            if self.config['w3c']:
                self.w3c_validator.validate()
            self.sitemap_validator.validate()
            self.robots_validator.validate()
