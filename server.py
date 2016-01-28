#!/usr/bin/env python
# coding:utf-8

import tornado.ioloop
import tornado.options
import tornado.httpserver
import tornado.autoreload

import sys

from application import application
from tornado.options import define, options
define("port", default=8888, help="run on th given port", type=int)

from methods.dbpool import install
DATABASE = {'mobile ip':  # connection name, used for getting connection from pool
            {'engine': 'mysql',      # db type, eg: mysql, sqlite
             'db': 'mobile ip',       # db table
             'host': '127.0.0.1',  # db host
             'port': 3306,        # db port
             'user': 'hao',      # db user
             'passwd': 'wh198910',  # db password
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
    instance = tornado.ioloop.IOLoop.instance()
    tornado.autoreload.start(instance)  # 修改代码自动加载无需重启app
    instance.start()

if __name__ == "__main__":
    main()
