#!/usr/bin/env python
# coding:utf-8
from optsql.dbpool import *
import tornado.web

import sys
reload(sys)
sys.setdefaultencoding('utf-8')


class IndexHandler(tornado.web.RequestHandler):

    @with_database("MobileTraceRoute")
    def get(self):
        lst = ["python"]
        ret = self.db.query("select count(*) from landmark_wuhan")
        print ret
        log.info('server=%s|name=%s|user=%s|addr=%s:%d|db=%s|idle=%d|busy=%d|max=%d|time=%d|ret=%s|num=%d|sql=%s|err=%s',
                 conn.type, conn.name, dbcf.get('user', ''),
                 dbcf.get('host', ''), dbcf.get('port', 0),
                 os.path.basename(dbcf.get('db', '')),
                 len(conn.pool.dbconn_idle),
                 len(conn.pool.dbconn_using),
                 conn.pool.max_conn,
                 int((endtm - starttm) * 1000000),
                 str(ret), num, repr(args[1]), err)

        self.render("index.html", info=lst)
