from mongoengine import Document, StringField, ObjectIdField, ReferenceField
from . import Language


class Author(Document):

    _id = ObjectIdField()
    name = StringField(required=True)
    url_name = StringField(required=True)
    language_id = ReferenceField(Language)

    def __init__(self, name, language_id, url_name):
        self.name = name
        self.language_id = language_id
        self.url_name = url_name

    def __str__(self):
        return "Name: " + self.name + " Language: " + self.language_id + " URL Name: " + self.url_name

    def set_author(self, name, language_id, url_name):
        self.name = name
        self.language_id = language_id
        self.url_name = url_name

    def set_name(self, name):
        self.name = name

    def set_language_id(self, language_id):
        self.language_id = language_id

    def set_url_name(self, url_name):
        self.url_name = url_name

    def get_author(self):
        return {
            "name": self.name,
            "language_id": self.language_id,
            "url_name": self.url_name
        }

    def get_name(self):
        return self.name

    def get_language_id(self):
        return self.language_id

    def get_url_name(self):
        return self.url_name
