#!/usr/local/bin/python
# coding: utf-8

import cgitb
cgitb.enable()
print("Content-Type: text/html; charset=UTF-8\n\n")

from wsgiref.handlers import CGIHandler
from appFlask import app
from sys import path

path.insert(0, '/rahydyn/www/api/hello/')
from appFlask import app
class ProxyFix(object):
  def __init__(self, app):
      self.app = app
  def __call__(self, environ, start_response):
      environ['SERVER_NAME'] = "rahydyn.sakura.ne.jp"
      environ['SERVER_PORT'] = "80"
      environ['REQUEST_METHOD'] = "GET"
      environ['SCRIPT_NAME'] = ""
      environ['PATH_INFO'] = "/"
      environ['SERVER_PROTOCOL'] = "HTTP/1.1"
      return self.app(environ, start_response)
if __name__ == '__main__':
   app.wsgi_app = ProxyFix(app.wsgi_app)
   CGIHandler().run(app)
