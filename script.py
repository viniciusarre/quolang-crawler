from main import Main
import tornado.web
from tornado.options import define, options
from api.Fetch import Fetch
from api.Index import Index
from util.logger import Logger

logger = Logger()

m = Main()
m.select_language()

define("port", default=6070, help="run on the given port", type=int)

if __name__ == "__main__":
    tornado.options.parse_command_line()
    logger.info("running on port >> " + str(options.port))
    app = tornado.web.Application([
        (r"/find", Fetch),
        (r"/", Index)

    ])
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
