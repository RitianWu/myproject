#!/usr/bin/env python
# coding:utf-8

from url import url

import tornado.web
import setting as setting_const
import os


setting = dict(
    template_path=setting_const.TEMPLATE_PATH,  # 模板路径
    static_path=setting_const.STATIC_PATH,  # 静态文件路径
    xsrf_cookies=setting_const.XSRF_COOKIES,  # 防跨站伪造请求
    cookie_secret=setting_const.COOKIE_SECRET,
    login_url=setting_const.LOGIN_URL,  # 登陆路径
    autoescape=setting_const.AUTOESCAPE,  # 自动转义
    debug=setting_const.DEBUG,  # 调试模式
)

application = tornado.web.Application(
    handlers=url,
    **setting
)
