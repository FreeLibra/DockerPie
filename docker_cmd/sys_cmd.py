#!/usr/bin/env python
# -*- coding:utf-8 -*-
import subprocess

LOG_DIR = './log/temp.txt'


def list_docker_images(log_dir=LOG_DIR):
    result = subprocess.getstatusoutput('docker images')
    # print(result[0])
    # print(result[1])
    with open(log_dir, 'w') as fp:
        fp.write(result[1])
    return result


if __name__ == '__main__':
    list_docker_images()
