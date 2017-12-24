"""
Debug版本,还在构思中
"""
# !/usr/bin/env python
# -*- coding:utf-8 -*-

import tornado.autoreload
import tornado.ioloop
import tornado.web
import docker_cmd.sys_cmd as cmd
from settings import settings


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        status, docker_images_title_list, docker_images_item_list = cmd.list_docker_images()
        self.render('base.html',
                    title='Welcome to use DockerPie',
                    docker_images_title_list=docker_images_title_list,
                    docker_image_item_list=docker_images_item_list,
                    items='')


def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
    ], **settings)


if __name__ == "__main__":
    app = make_app()
    app.listen(8888, address='0.0.0.0')
    tornado.ioloop.IOLoop.current().start()
