class Result:
    def __init__(self):
        self.broken_urls = {} #
        self.inbound_counter = {} #
        self.outbound_counter = {} #
        self.url_counter = {} #
        self.urls_302 = {} #
        self.http_urls = [] #
        self.urls_missing_title = [] #
        self.urls_wrong_chars = [] #
        self.repeated_titles = {}
        self.page_missing_title = []
        self.titles_wrong_size = []
        self.description_missing = []
        self.repeated_descriptions = {}
        self.description_wrong_size = []
        self.title_wrong_chars = []
        self.heading_too_many = {}
        self.heading_missing = []
        self.heading_structure = []
        self.little_content = {}
        self.missing_robots = False
        self.missing_sitemap = False
        self.alt_text_missing = {}
        self.no_open_graph = []
        self.time_to_first_byte = 0
        self.fct = 0

    def show(self):
        self.time_results()
        self.sitemap_results()
        self.robots_results()
        self.open_graph_results()
        self.description_results()
        self.alt_text_results()
        self.content_results()
        self.headings_results()
        self.title_results()

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
            print("On page " + str(i) + " too many(" + str(
                self.inbound_counter[i]) + ") inbound links were found.")

        print("")
        for i in self.outbound_counter:
            print("On page " + str(i) + " too many(" + str(
                self.outbound_counter[i]) + ") outbound links were found.")

        print("")
        print("Found " + str(len(self.http_urls)) + " not HTTPS urls:")
        for i in self.http_urls:
            print(" ------> " + str(i))

        print("")
        print("Found " + str(len(self.urls_missing_title)) + " <a> tags with missing title: ")
        for i in self.urls_missing_title:
            print(" ------> " + str(i))

        print("")
        print("Found " + str(
            len(self.urls_wrong_chars)) + " urls with not recommended characters (\"_\", \" \" or uppercase): ")
        for i in self.urls_wrong_chars:
            print(" ------> " + str(i))


    def title_results(self):
        print("")
        print("Found " + str(len(self.page_missing_title)) + " pages with missing titles: ")
        for i in self.page_missing_title:
            print(" ------> " + str(i))

        for i in self.repeated_titles:
            if len(self.repeated_titles[i]) > 1:
                print("")
                print("Repeated title: ")
                print(" \"" + str(i) + "\" on pages:")
                for j in self.repeated_titles[i]:
                    print(" ------> " + str(j))

        print("")
        print("Found " + str(len(self.titles_wrong_size)) + " titles with not recommended length on pages: ")
        for i in self.titles_wrong_size:
            print(" ------> " + str(i))

        print("")
        print("Found titles with not recommended characters (\' , \', \' ' \', \' \" \') on pages: ")
        for i in self.title_wrong_chars:
            print(" ------> " + str(i))

    def description_results(self):
        print("")
        print("Found " + str(len(self.description_missing)) + " pages with missing description: ")
        for i in self.description_missing:
            print(" ------> " + str(i))

        for i in self.repeated_descriptions:
            if len(self.repeated_descriptions[i]) > 1:
                print("")
                print("Repeated description: ")
                print(" \"" + str(i) + "\" on pages:")
                for j in self.repeated_descriptions[i]:
                    print(" ------> " + str(j))

        print("")
        print("Found " + str(len(self.description_wrong_size)) + " descriptions with not recommended length on pages: ")
        for i in self.description_wrong_size:
            print(" ------> " + str(i))

    def headings_results(self):
        print("")
        print("Found " + str(len(self.heading_missing)) + " pages without h1 heading: ")
        for i in self.heading_missing:
            print(" ------> " + str(i))

        print("")
        for i in self.heading_too_many:
            print("On page " + str(i) + " found too many h1 headings:")
            for j in self.heading_too_many[i]:
                print("     " + str(j))


        print("Found " + str(len(self.heading_structure)) + " pages with wrong structure of headings:")
        for i in self.heading_structure:
            print(i)

    def content_results(self):
        print("")
        for i in self.little_content:
            print("On page  " + str(i) + " there is too little content (" + str(self.little_content[i]) + " characters).")

    def robots_results(self):
        print("")
        if self.missing_robots:
            print("Missing robots.txt")

    def sitemap_results(self):
        print("")
        if self.missing_sitemap:
            print("Missing sitemap.xml")

    def alt_text_results(self):
        print("")
        for i in self.alt_text_missing:
            print("Found " + str(self.alt_text_missing[i]) + " graphics without alt text on page " + str(i))

    def open_graph_results(self):
        print("")
        print("Open Graph Object not found on pages:")
        for i in self.no_open_graph:
            print(" ------> " + str(i))

    def time_results(self):
        if self.fct < 1000:
            speed = "fast"
        elif self.fct < 3000:
            speed = "moderate"
        else:
            speed = "slow"
        print("")
        print(f'Site response time is {self.time_to_first_byte} ms.')
        print(f'It took {self.fct} ms to load first website content which is {speed}.')
