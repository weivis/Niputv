from tornado.wsgi import WSGIContainer
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop

from app import app, blueprint

http_server = HTTPServer(WSGIContainer(app))
http_server.listen(8003)
IOLoop.instance().start()