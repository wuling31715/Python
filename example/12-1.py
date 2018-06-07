# _*_ coding: utf-8 _*_
# 程式 12-1 (Python 3 Version)

import requests, json
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

url = "https://graph.facebook.com/v2.8/me/posts?access_token=EAACEdEose0cBAPnoSaYZCTXvAb3Mm7soaSrXZAu4rkuI8y9CkcEJ5YVdtt1Om7wsocoQzmrzl9qwC1UdDUdAgPuZAfxRkTu6VAZCku7KmfGU4AqjfMIcZBZCY9ZCgD6zkUSBUaQygIMMjnaiutnenz0U5j7SFnubD8SU51Yctv7ZCmibJ4XQySTPXHBUwjuGVqDwm97sGZAwnSQZDZD"
res = requests.get(url)

data = json.loads(res.text)
for d in data['data']:
	if 'message' in d:
		message = d['message']
		print d['created_time'], message.encode('UTF8')
		print('----------------------------------')
