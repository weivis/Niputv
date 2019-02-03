import tornado.httpserver
import tornado.ioloop
import loop
from business import video_countAPI, bangumi_countAPI, datawc, getcount

if __name__ == "__main__":

    app = tornado.web.Application(
        handlers=[
            (r"/api/video/count/(.*)/(.*)", video_countAPI),
            (r"/api/bangumi/count/(.*)/(.*)", bangumi_countAPI),
            (r"/api/get", datawc),
            (r"/api/getcount", getcount),
        ],
        debug=True
    )

    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(8004, address="127.0.0.1")
    tornado.ioloop.IOLoop.current().start()