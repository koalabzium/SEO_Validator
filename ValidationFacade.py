from CrawlingAndValidating.URLValidator import URLValidator
from CrawlingAndValidating.ContentValidator import ContentValidator
from CrawlingAndValidating.Result import Result


class ValidationFacade:

    def __init__(self, content, url, starting_url, result):
        self.url_validator = URLValidator(url, result)
        self.content_validator = ContentValidator(url, content, result)
        self.result = result

    def validate(self):
        self.url_validator.validate()
        self.content_validator.validate()
        self.show_result()

    def create_result(self):
        pass

    def show_result(self):
        print("")
        for i in self.result.broken_urls:
            print("Found " + str(len(self.result.broken_urls[i])) + " broken urls on page " + str(i) + ":")
            for j in self.result.broken_urls[i]:
                print(" ------> " + str(j))
            print("")

        if self.result.urls_302 != {}:
            print("302 URLs: ")
        for i in self.result.urls_302:
            print(" On page " + str(i) + " those URLs return 302 status code. If it is possible change them for 301:")
            for j in self.result.urls_302[i]:
                print(" ------> " + str(j))
            print("")


        for i in self.result.url_counter:
            print("On page " + str(i) + " too many(" + str(self.result.url_counter[i]) + ") links were found.")

        print("")
        for i in self.result.inbound_counter:
            print("On page " + str(i) + " too many(" + str(self.result.inbound_counter[i]) + ") inbound links were found.")

        print("")
        for i in self.result.outbound_counter:
            print("On page " + str(i) + " too many(" + str(self.result.outbound_counter[i]) + ") outbound links were found.")

        print("")
        print("Found " + str(len(self.result.http_urls)) + " not HTTPS urls:")
        for i in self.result.http_urls:
            print(" ------> " + str(i))

        print("")
        print("Found " + str(len(self.result.urls_missing_title)) + " <a> tags with missing title: ")
        for i in self.result.urls_missing_title:
            print(" ------> " + str(i))

        print("")
        print("Found " + str(len(self.result.urls_wrong_chars)) + " urls with not recommended characters (\"_\", \" \" or uppercase): ")
        for i in self.result.urls_wrong_chars:
            print(" ------> " + str(i))
