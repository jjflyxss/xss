#!/usr/bin/env python
# -*- coding:utf-8 -*-

__author__ = 'r0ker'

from sockjs.tornado.transports import base
from sockjs.tornado import conn
import db
import json


class SockConnection(conn.SockJSConnection):
	participants = set()
		
	def on_open(self, info):
		cookie = base.BaseTransportMixin.sock_cookies
		row = db.ct("manager", "*", "username='"+cookie['username']+"' and password='"+cookie['password']+"'")
		if row:
			self.name = 'manager'
		else:
			hostip = base.BaseTransportMixin.sock_remote_ip
			self.name = hostip
		self.participants.add(self)



	def on_message(self, message):
		if self.name == 'manager':
			message = json.loads(message)
			self.broadcast(filter(lambda x:x.name == message['hostip'], self.participants), message['msg'])
		else:
			try:
				db.i('msglog',"msg","'"+message+"'")
			except Exception,e:
				self.send(str(e))
			self.broadcast(filter(lambda x:x.name == 'manager', self.participants), message)




