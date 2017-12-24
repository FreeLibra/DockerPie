#!/usr/bin/env python
# -*- coding:utf-8 -*-
import subprocess
import numpy as np

LOG_DIR = './log/temp.txt'


def list_docker_images(log_dir=LOG_DIR):
    result = subprocess.getstatusoutput('docker images')
    # print(result[0])
    # print(result[1])
    with open(log_dir, 'w') as fp:
        fp.write(result[1])
    line_list = result[1].split('\n')
    print(line_list[0])
    word = line_list[0]
    print(word)
    print(len(word))
    print(type(word))
    # print('------------')
    # for ele in word:
    #     print(ele)
    return result


if __name__ == '__main__':
    list_docker_images()
