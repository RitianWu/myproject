#!/usr/bin/env python
# coding:utf-8

import tornado.ioloop
import tornado.options
import tornado.httpserver

import sys

from application import application
from tornado.options import define, options
define("port", default=8888, help="run on th given port", type=int)

from optsql.dbpool import install
DATABASE = {'MobileTraceRoute':  # connection name, used for getting connection from pool
            {'engine': 'mysql',      # db type, eg: mysql, sqlite
             'db': 'MobileTraceRoute',       # db table
             'host': '123.56.225.227',  # db host
             'port': 3306,        # db port
             'user': 'root',      # db user
             'passwd': 'litengfei2013*',  # db password
             'charset': 'utf8',  # db charset
             'conn': 10}          # db connections in pool
            }
install(DATABASE)


def main():
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(options.port)
    print 'Development server is running at http://127.0.0.1:%s/' % options.port
    print 'Quit the server with Control-C'
    tornado.ioloop.IOLoop.instance().start()

if __name__ == "__main__":
    main()
