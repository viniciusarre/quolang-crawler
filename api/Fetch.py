import tornado.web
from fetch.fr import French
from util.logger import Logger

logger = Logger()


class Fetch(tornado.web.RequestHandler):

    def get(self):
        """
            GET method for Fetch handler. 
            Fetches new quotes for a given author and then returns a boolean in case the request was successful
        """
        try:
            author = self.get_query_argument("author", strip=False)
            if author is not None:
                author = author.replace(" ", "_")
                f = French()
                logger.info('***** looking for ******* ' + author)
                res = f.url_set_up(author, "fr")
                if res["status"]:
                    self.write({"success": True})
                else:
                    self.write({"success": False})
        except:
            self.write({"success": False})
    def set_default_headers(self):
        """
            Set default headers for the requests
        """
        logger.info("setting headers!!!")
        self.set_header("Access-Control-Allow-Origin", "*")
        self.set_header("Access-Control-Allow-Headers", "x-requested-with")
        self.set_header('Access-Control-Allow-Methods', 'POST, GET, OPTIONS')
