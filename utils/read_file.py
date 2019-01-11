# -*- coding: utf-8 -*-
def read_file(path):
    with open(path, mode='r') as f:
        text = f.read()
    return text
