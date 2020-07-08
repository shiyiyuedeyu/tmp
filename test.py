# -*- coding: utf-8 -*-
import urllib2
import urllib
import time
#http_url='https://api-cn.faceplusplus.com/facepp/v3/detect'
http_url='https://api-cn.faceplusplus.com/facepp/v1/3dface'
key = "_q3uQ33z3SFxtXvJfBObGDsuK3Guzp4y"
secret = "nrHH1FoJZKQIJSYZopInQpesWWS4O7bd"
filepath = r"./1.jpg"
boundary = '----------%s' % hex(int(time.time() * 1000))
data = []
data.append('--%s' % boundary)
data.append('Content-Disposition: form-data; name="%s"\r\n' % 'api_key')
data.append(key)
data.append('--%s' % boundary)
data.append('Content-Disposition: form-data; name="%s"\r\n' % 'api_secret')
data.append(secret)
data.append('--%s' % boundary)
fr=open(filepath,'rb')
data.append('Content-Disposition: form-data; name="%s"; filename=" "' % 'image_file')
data.append('Content-Type: %s\r\n' % 'application/octet-stream')
data.append(fr.read())
fr.close()
data.append('--%s' % boundary)
data.append('Content-Disposition: form-data; name="%s"\r\n' % 'return_landmark')
data.append('1')
data.append('--%s' % boundary)
data.append('Content-Disposition: form-data; name="%s"\r\n' % 'return_attributes')
data.append("gender,age,smiling,headpose,facequality,blur,eyestatus,emotion,ethnicity,beauty,mouthstatus,eyegaze,skinstatus")
data.append('--%s--\r\n' % boundary)

http_body='\r\n'.join(data)
#buld http request
req=urllib2.Request(http_url)
#header
req.add_header('Content-Type', 'multipart/form-data; boundary=%s' % boundary)
req.add_data(http_body)
try:
	#req.add_header('Referer','http://remotserver.com/')
	#post data to server
	resp = urllib2.urlopen(req, timeout=5)
	#get response
	qrcont=resp.read()
	print qrcont

except urllib2.HTTPError as e:
    print e.read()
