#!/usr/bin/env python
# -*- coding:utf-8 -*-  

__author__ = 'r0ker'
import urllib
import urllib2
import json
import time
import db



def urljson(data):
	print urlde(data)
	return json.loads(urlde(data))


def timede(t):
	return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(t))


def urlde(str):
	str = str.encode('utf-8')
	return urllib.unquote(str)


def urlen(str):
	str = str.encode('utf-8')
	return urllib.quote(str).replace("%", "%%")


def md5(str):
	import hashlib
	m = hashlib.md5()
	m.update(str)
	return m.hexdigest()


def getaddr(ip):
	url = 'http://ip.taobao.com/service/getIpInfo.php?ip='+ip
	req = urllib2.Request(url)
	res_data = None
	while  res_data == None:
		try:
			res_data = urllib2.urlopen(req).read()
		except:
			pass
	res_data = json.loads(res_data)
	addr = '-'.join((res_data['data']['country'],res_data['data']['region'],res_data['data']['city'],res_data['data']['county'],res_data['data']['isp']))
	db.u('host',"addr = '"+addr + "'","hostip='"+ip+"'")
	return addr



