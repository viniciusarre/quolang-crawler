from main import Main
import tornado.web
from tornado.options import define, options
from dev.api.Fetch import Fetch

m = Main()
m.selectLanguage()


define("port", default=6070, help="run on the given port", type=int)

if __name__ == "__main__":
    tornado.options.parse_command_line()
    print("running on port >> " + str(options.port))
    app = tornado.web.Application(handlers=[
        (r"/find/", Fetch)])
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
