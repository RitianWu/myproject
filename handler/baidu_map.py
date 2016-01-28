#!/usr/bin/env python
# coding:utf-8
from methods.dbpool import *

import tornado.web
import logging
try:
    import simplejson as json
except ImportError:
    import json

import sys
reload(sys)
sys.setdefaultencoding('utf-8')
log = logging.getLogger()


class MapHandler(tornado.web.RequestHandler):

    @with_database('mobile ip')
    def get(self):
        target_ip = "61.158.148.2"
        where = {
            'ip': target_ip
        }
        fields = ['ip', 'lat', 'lon']
        ret = self.db.select("rtb_history", where=where, fields=fields)
        rtb_history = [','.join([ip_ll['lon'], ip_ll['lat']]) for ip_ll in ret]
        print "the number of point: ", len(rtb_history)
        self.render("baidu_map.html", ip=target_ip, num=len(
            rtb_history), points=json.dumps(rtb_history))

    def post(self):
        return
