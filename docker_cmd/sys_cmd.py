#!/usr/bin/env python
# -*- coding:utf-8 -*-
import subprocess
import numpy as np
import pandas as pd
import re

LOG_FILE = './log/temp.txt'


def result_handler(raw_output, log_file=LOG_FILE):
    """
    Handle the raw_output words in lines
    word = re.sub("[^\w]", " ", line).split()
    word = re.sub("\s", " ", line).split()
    :param raw_output: raw_output words in lines from the terminal
    :param log_dir: the output temp file
    :return:
    """
    with open(log_file, 'w') as fp:
        fp.write(raw_output[1])
    result_item_list = []
    line_list = raw_output[1].split('\n')
    print(line_list)
    for line in line_list:
        result_item_list.append(re.sub("\s{2,}", "\t", line).split("\t"))
    print(result_item_list)
    return raw_output[0], result_item_list


def list_docker_images(log_file=LOG_FILE):
    """
    list the docker images
    :return: status,the items in docker images  list
    """
    raw_result = subprocess.getstatusoutput('docker images')
    return result_handler(raw_result, log_file=LOG_FILE)


if __name__ == '__main__':
    list_docker_images()
