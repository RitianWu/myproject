#!/usr/bin/env python
# coding:utf-8

from url import url

import tornado.web
import os
import base64
import uuid

secretKey = base64.b64encode(uuid.uuid4().bytes + uuid.uuid4().bytes)

setting = dict(
    template_path=os.path.join(os.path.dirname(__file__), "template"),
    static_path=os.path.join(os.path.dirname(__file__), "static"),
    cookie_secret=secretKey,  # cookie“加密”
    xsrf_cookies=True,  # 开启XSRF保护
    login_url='/',  # 如果当前用户没登录，会找到该目录
)

application = tornado.web.Application(
    handlers=url,
    **setting
)
