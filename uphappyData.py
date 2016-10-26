# -*- coding: UTF-8 -*-
import urllib2
import urllib
import json
import httplib
def patch_httplib():
	prev_request = httplib.HTTPConnection.request
	def request(self,method,url,body=None,headers={}):
		if 'Userkey'in headers:
			v=headers['Userkey']
			del headers['Userkey']
			headers['userkey'] = v
			
		self._send_request(method,url,body,headers)
	httplib.HTTPConnection.request = request
	httplib.HTTPConnection.prev_request = prev_request

patch_httplib()


# class Myrequest(urllib2.Request):
	# def add_header(self,key,val):
		# self.headers[key]=val

		
		
proxy = urllib2.ProxyHandler({'http':'127.0.0.1:8888'})#Fiddle 
cookies = urllib2.HTTPCookieProcessor() 
# wopen = Myopener(cookies,proxy)
way=['UpdateSensors','excutecommand']
url="http://www.lewei50.com/api/V1/gateway/UpdateSensors/02"#乐联网传感器
#定义要提交的数据
postdata={'Name':'T1','Value':10}
postdata2={'Name':'01H1','Value':10} #准备json
data=[postdata,postdata2]
jdata=json.dumps(data)
# postdata=urllib.urlencode(postdata)
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
headers = { 'userkey':'50d354a2812644bc83735a188f4d82ba' }

# requests.get(url,headers)
request = urllib2.Request(url,jdata,headers=headers)
response=urllib2.urlopen(request)
print response.read()

# wopen.open(request)








