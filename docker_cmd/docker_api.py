#!/usr/bin/env python
# -*- coding:utf-8 -*-

import docker

client = docker.from_env()


def list_docker_images():
    i = 0
    for image in client.images.list():
        print(str(i) + '-----------------------------')
        print(image.id)
        print(image.short_id)
        print(image.id_attribute)
        print(image.client)
        print(image)
        print(image.attrs)
        print(image.attrs['Created'])
        print('-----------------------------------')
        i += 1


if __name__ == '__main__':
    list_docker_images()
