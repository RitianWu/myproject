#!/usr/bin/env python
#coding:utf-8

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

from handler.index import IndexHandler
from handler.baidu_map import MapHandler

url=[
    (r'/', IndexHandler),
    (r'/map', MapHandler),
    ]
