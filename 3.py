#带参数访问网页
import requests

data = {
    'name' : 'germey',
    'age' : 22
}

r = requests.get('http://httpbin.org/get' ,params=data)

print(r.text)
print(r.json())  #json格式打印 返回字典类型
