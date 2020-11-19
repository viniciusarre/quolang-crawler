class Language:
    def __init__(self, code, name):
        self.code = code
        self.name = name

    def set_language(self, code, name):
        self.code = code
        self.name = name

    def set_code(self, code):
        self.code = code

    def set_name(self, name):
        self.name = name

    def get_language(self):
        return {
            "code": self.code,
            "name": self.name
        }

    def get_code(self):
        return self.code

    def get_name(self):
        return self.name
