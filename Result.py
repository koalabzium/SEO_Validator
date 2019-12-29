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

