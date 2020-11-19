class Source:
    def __init__(self, source_text, language_id):
        self.source_text = source_text
        self.language_id = language_id

    def set_source(self, source_text, language_id):
        self.source_text = source_text
        self.language_id = language_id

    def set_source_text(self, source_text):
        self.source_text = source_text

    def set_language_id(self, language_id):
        self.language_id = language_id

    def get_source(self):
        return {
            "source_text": self.source_text,
            "language_id": self.language_id
        }

    def get_source_text(self):
        return self.source_text

    def get_language_id(self):
        return self.language_id
