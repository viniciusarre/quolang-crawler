from tornado.web import RequestHandler, StaticFileHandler

import os

path = os.path.dirname("./static/")


class Index (RequestHandler):
    def get(self):
        self.render(path + "/index.html")

    def set_default_headers(self):
        print("setting headers!!!")
        self.set_header("Access-Control-Allow-Origin", "*")
        self.set_header("Access-Control-Allow-Headers", "x-requested-with")
        self.set_header('Access-Control-Allow-Methods', 'POST, GET, OPTIONS')
