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
        self.heading_missing = []
        self.heading_structure = []

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

        print("")
        print("Found " + str(len(self.heading_structure)) + " pages with wrong structure of headings:")
        for i in self.heading_structure:
            print(i)



    def show(self):
        self.title_results()
        self.description_results()
        self.headings_results()
