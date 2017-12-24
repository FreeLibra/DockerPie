#!/usr/bin/env python
# -*- coding:utf-8 -*-
import subprocess
import numpy as np
import pandas as pd
import re
import os
from settings import cmd_log_file_path


def write_log(content):
    with open(cmd_log_file_path, 'w') as fp:
        fp.write(content)


def result_handler(raw_output):
    """
    Handle the raw_output words in lines
    :param raw_output: raw_output words in lines from the terminal
    :param log_dir: the output temp file
    :return:
    """
    write_log(raw_output[1])
    item_list = []
    line_list = raw_output[1].split('\n')
    title_list = re.sub("\s{2,}", "\t", line_list[0]).split("\t")
    for line in line_list[1:]:
        item_list.append(re.sub("\s{2,}", "\t", line).split("\t"))
    return raw_output[0], title_list, item_list


def list_docker_images():
    """
    list the docker images
    :return: status,the items in docker images  list
    """
    raw_result = subprocess.getstatusoutput('docker images')
    return result_handler(raw_result)


if __name__ == '__main__':
    list_docker_images()
