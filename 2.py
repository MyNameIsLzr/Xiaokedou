#简单的网页访问

import requests

'''
r = requests.get('http://httpbin.org/get')

http://httpbin.org/get该网站会判断如果客户端发起的是GET请求的话，
它返回相应的请求信息



'''
r = requests.get('https://www.baidu.com/')

#r = requests.post('https://www.baidu.com/')

#r = requests.put('https://www.baidu.com/')

#r = requests.delete('https://www.baidu.com/')

#r = requests.head('https://www.baidu.com/')

#r = requests.options('https://www.baidu.com/')

print(type(r))  #返回类型

print(r.status_code) #返回状态

print(type(r.text))  #返回页面响应体的类型

print(r.text) #抓取页面的源代码

print(r.cookies) #返回Cookies的类型
