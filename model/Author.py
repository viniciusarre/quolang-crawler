
class Author:
    name = ''
    language = ''
    url_name = ''

    def __init__(self, name, language, url_name):
        self.name = name
        self.language = language
        self.url_name = url_name

    def __str__(self):
        return "Name: " + self.name + " Language: " + self.language + " URL Name: " + self.url_name

    def set_author(self, name, language, url_name):
        self.name = name
        self.language = language
        self.url_name = url_name

    def set_name(self, name):
        self.name = name

    def set_language(self, language):
        self.language = language

    def set_url_name(self, url_name):
        self.url_name = url_name

    def get_author(self):
        return {
            "name": self.name,
            "language": self.language,
            "url_name": self.url_name
        }

    def get_name(self):
        return self.name

    def get_language(self):
        return self.language

    def get_url_name(self):
        return self.url_name
