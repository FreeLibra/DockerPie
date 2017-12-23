# -*- coding:utf-8 -*-

import tornado.ioloop
import tornado.web
from docker_cmd.sys_cmd import *

LOG_DIR = './docker_cmd/log/temp.txt'


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        images_list = list_docker_images(log_dir=LOG_DIR)
        self.write(str(images_list[1]))


def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
    ])


if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
