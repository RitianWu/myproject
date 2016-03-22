# -*- coding:utf-8 -*-

import os
import base64
import uuid

# Server
SERVER_PORT = 8888
TEMPLATE_PATH = os.path.join(os.path.dirname(__file__), "template")
STATIC_PATH = os.path.join(os.path.dirname(__file__), "static")
XSRF_COOKIES = True
COOKIE_SECRET = base64.b64encode(uuid.uuid4().bytes + uuid.uuid4().bytes)
LOGIN_URL = "/login"
AUTOESCAPE = None
DEBUG = True
