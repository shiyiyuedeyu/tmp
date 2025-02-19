# -*- coding: utf-8 -*-
import urllib.request
import urllib.error
import time
import json
import base64
#import requests

http_url = 'https://api-cn.faceplusplus.com/facepp/v1/3dface'
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
fr = open(filepath, 'rb')
data.append('Content-Disposition: form-data; name="%s"; filename=" "' % 'image_file_1')
data.append('Content-Type: %s\r\n' % 'application/octet-stream')
data.append(fr.read())
fr.close()
data.append('--%s' % boundary)
data.append('Content-Disposition: form-data; name="%s"\r\n' % 'return_landmark')
data.append('1')
data.append('--%s' % boundary)
data.append('Content-Disposition: form-data; name="%s"\r\n' % 'return_attributes')
data.append(
    "gender,age,smiling,headpose,facequality,blur,eyestatus,emotion,ethnicity,beauty,mouthstatus,eyegaze,skinstatus")
data.append('--%s--\r\n' % boundary)

for i, d in enumerate(data):
    if isinstance(d, str):
        data[i] = d.encode('utf-8')

http_body = b'\r\n'.join(data)

# build http request
req = urllib.request.Request(url=http_url, data=http_body)

# header
req.add_header('Content-Type', 'multipart/form-data; boundary=%s' % boundary)

try:
    # post data to server
    resp = urllib.request.urlopen(req, timeout=5)
    # get response
    qrcont = resp.read()
    #with open("code2.zip", "wb") as code:
    #    code.write(qrcont)
    # if you want to load as json, you should decode first,
    # for example: json.loads(qrount.decode('utf-8'))
    data = json.loads(qrcont.decode('utf-8'))
    print(data['request_id'])
    with open("face.obj", "wb") as code:
        code.write(base64.b64decode(data['obj_file'].encode('utf-8')))
    # print(qrcont.decode('utf-8'))
except urllib.error.HTTPError as e:
    print(e.read().decode('utf-8'))
