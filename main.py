import tornado.web
from tornado import ioloop
from tornado import httpserver
from tornado.web import Application

from controller.controller_produto import Index, Novo, Deletar, Alterar


class App(Application):

    def __init__(self):
        urls = [
            (r'/', Index),
            (r'/produto/novo', Novo),
            (r'/produto/deletar/(\d+)', Deletar),
            (r'/produto/alterar/(\d+)', Alterar),
        ]

        settings = dict(
            debug=True,
            template_path='views',
        )

        Application.__init__(self, urls, **settings)


if __name__ == "__main__":
    http_server = tornado.httpserver.HTTPServer(App())
    http_server.listen(8000)
    tornado.ioloop.IOLoop.current().start()
