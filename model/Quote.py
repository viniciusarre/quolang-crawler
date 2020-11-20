from mongoengine import Document, StringField, ObjectIdField, ReferenceField
from . import Language


class Quote(Document):

    _id = ObjectIdField()
    phrase = StringField(required=True)
    language_id = ReferenceField(Language)

    def __init__(self, phrase, language_id):
        self.phrase = phrase
        self.language_id = language_id

    def get_quote(self):
        return {
            "phrase": self.phrase,
            "language_id": self.language_id
        }

    def get_phrase(self):
        return self.phrase

    def get_language_id(self):
        return self.language_id

    def set_quote(self, phrase, language_id):
        self.language_id = language_id
        self.phrase = phrase

    def set_phrase(self, phrase):
        self.phrase = phrase

    def set_language_id(self, language_id):
        self.language_id = language_id
