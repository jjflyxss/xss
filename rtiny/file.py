#!/usr/bin/env python
# -*- coding:utf-8 -*-

__author__ = 'r0ker'

import tornado.web
from base import BaseHandler
import os,db
from config import URL
from function import urlde

class FileHandler(BaseHandler):
	@tornado.web.authenticated
	def get(self):
		files =  os.popen('dir').readlines()
		self.render(
			"file.html",
			heads=[
				{'name':'file', 'title':'', 'url':''},
			],
			username=self.get_secure_cookie("username"),
			datainfo=db.datainfo(),
			url=URL,
			urlde=urlde,
			files = files,
		)