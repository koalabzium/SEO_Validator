from CrawlingAndValidating.Validator import Validator
import requests


class SpeedValidator(Validator):
    def __init__(self, url, result):
        self.url = url
        self.result = result

    def validate(self):
        x = "https://www.googleapis.com/pagespeedonline/v5/runPagespeed?url=" + str(self.url)
        r = requests.get(x)
        final = r.json()
        try:
            time_to_first_byte = final['lighthouseResult']['audits']['time-to-first-byte']['numericValue']
            fct = final['lighthouseResult']['audits']['first-contentful-paint']['numericValue']
            self.result.time_to_first_byte = time_to_first_byte
            self.result.fct = fct
        except KeyError:
            print("Unable to get site speed")
