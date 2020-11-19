class Quote:

    def __init__(self, phrase, language):
        self.phrase = phrase
        self.language = language

    def get_quote(self):
        return {
            "phrase": self.phrase,
            "language": self.language
        }

    def get_phrase(self):
        return self.phrase

    def get_language(self):
        return self.language

    def set_quote(self, phrase, language):
        self.language = language
        self.phrase = phrase

    def set_phrase(self, phrase):
        self.phrase = phrase

    def set_language(self, language):
        self.language = language
