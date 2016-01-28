# coding=utf-8

import tornado.web
import tornado.escape

from methods.dbpool import *
from base import BaseHandler


class UserHandler(BaseHandler):

    @tornado.web.authenticated
    @with_database("mobile ip")
    def get(self):
        #username = self.get_argument('user')
        username = tornado.escape.json_decode(self.current_user)
        user_infos = self.db.select_one(
            "users", where={'username': username})
        print user_infos
        self.render('user.html', users=user_infos)
