class URLResult(object):

    def __init__(self):
        self.broken_urls = {}
        self.inbound_counter = {}
        self.outbound_counter = {}
        self.url_counter = {}
        self.urls_302 = {}
        self.http_urls = []
        self.urls_missing_title = []
        self.urls_wrong_chars = []

    def show(self):
        print("")
        for i in self.broken_urls:
            print("Found " + str(len(self.broken_urls[i])) + " broken urls on page " + str(i) + ":")
            for j in self.broken_urls[i]:
                print(" ------> " + str(j))
            print("")

        if self.urls_302 != {}:
            print("302 URLs: ")
        for i in self.urls_302:
            print(" On page " + str(i) + " those URLs return 302 status code. If it is possible change them for 301:")
            for j in self.urls_302[i]:
                print(" ------> " + str(j))
            print("")


        for i in self.url_counter:
            print("On page " + str(i) + " too many(" + str(self.url_counter[i]) + ") links were found.")

        print("")
        for i in self.inbound_counter:
            print("On page " + str(i) + " too many(" + str(self.inbound_counter[i]) + ") inbound links were found.")

        print("")
        for i in self.outbound_counter:
            print("On page " + str(i) + " too many(" + str(self.outbound_counter[i]) + ") outbound links were found.")

        print("")
        print("Found " + str(len(self.http_urls)) + " not HTTPS urls:")
        for i in self.http_urls:
            print(" ------> " + str(i))

        print("")
        print("Found " + str(len(self.urls_missing_title)) + " <a> tags with missing title: ")
        for i in self.urls_missing_title:
            print(" ------> " + str(i))

        print("")
        print("Found " + str(len(self.urls_wrong_chars)) + " urls with not recommended characters (\"_\", \" \" or uppercase): ")
        for i in self.urls_wrong_chars:
            print(" ------> " + str(i))
