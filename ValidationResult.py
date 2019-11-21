class ValidationResult(object):
    def __init__(self):
        self.repeated_titles = {}
        self.page_missing_title = []
        self.titles_wrong_size = []
        self.description_missing = []
        self.repeated_descriptions = {}
        self.description_wrong_size = []
        self.title_wrong_chars = []
        self.heading_too_many = {}

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

    def show(self):
        self.title_results()
        self.description_results()
