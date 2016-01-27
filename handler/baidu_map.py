#!/usr/bin/env python
# coding:utf-8
from optsql.dbpool import *

import tornado.web
import logging

import sys
reload(sys)
sys.setdefaultencoding('utf-8')
log = logging.getLogger()


class MapHandler(tornado.web.RequestHandler):

    @with_database('MobileTraceRoute')
    def get(self):
        # lst = ["python","www.itdiffer.com","qiwsir@gmail.com"]
        # self.render("index.html", info=lst)
        ret = self.db.query("select count(*) from landmark_wuhan")
        print ret
        self.render("baidu_map.html")

    def post(self):
        return
