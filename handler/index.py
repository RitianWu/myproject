#!/usr/bin/env python
# coding:utf-8
from tools.dbpool import *
import tornado.web

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

from base import BaseHandler


class IndexHandler(tornado.web.RequestHandler):

    @with_database("mobile ip")
    def get(self):
        usernames = self.db.select_one("users", fields="username")
        one_user = usernames["username"]
        self.render("index.html", user=one_user)

    @with_database("mobile ip")
    def post(self):
        username = self.get_argument("username")
        password = self.get_argument("password")
        user_infos = self.db.select_one(
            "users", where={'username': username})
        if user_infos:
            db_pwd = user_infos["password"]
            if db_pwd == password:
                self.set_current_user(username)  # 设置cookie
                self.write(username)
            else:
                self.write("Your password was not right.")
        else:
            self.write("There is no this user.")

    def set_current_user(self, user):
        if user:
            self.set_secure_cookie('user', tornado.escape.json_encode(user))
        else:
            self.clear_cookie('user')


class ErrorHandler(BaseHandler):

    def get(self):
        self.render("error.html")
