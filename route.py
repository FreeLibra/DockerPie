"""
Debug版本,还在构思中
"""
# !/usr/bin/env python
# -*- coding:utf-8 -*-

import tornado.autoreload
import tornado.ioloop
import tornado.web
from docker_cmd.sys_cmd import list_docker_images
from settings import settings

LOG_DIR = './docker_cmd/log/temp.txt'


# def handle_request(client):
#     buf = client.recv(1024)
#     client.send("HTTP/1.1 200 OK\r\n\r\n")
#     client.send("Hello, Seven")


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        images_list = list_docker_images(log_dir=LOG_DIR)
        # self.write('\n输出本地Docker镜像列表:\n\n')
        # self.write(str(images_list[1]))
        self.render('base.html', title='Welcome to use DockerPie', items='Hello')


def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
    ], **settings)


if __name__ == "__main__":
    app = make_app()
    app.listen(8888, address='0.0.0.0')
    tornado.ioloop.IOLoop.current().start()
