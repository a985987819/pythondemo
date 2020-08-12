import requests

# 主动跑出代码异常
bad_r = requests.get('http://httpbin.org/status/404')
print(bad_r.status_code)
# bad_r.raise_for_status()

#使用requests.Session对象请求
#创建Session对象
s = requests.Session()
#session对象会保存服务器返回的set-cookies头信息里面的内容
s.get('http://httpbin.org/cookies/set/userid/123456789')
s.get('http://httpbin.org/cookies/set/tokeen/xxxxxxxxxx')
#下次请求会将本地所有的cookies信息自动添加到请求头信息里
r = s.get('http://httpbin.org/cookies')
print('检查session中的cookies',r.json())

#使用ddli
print('不适用代理',requests.get('http://httpbin.org/ip').json())
print('使用代理',requests.get(
    'http://httpbin.org/ip',
    proxies = {'http:':'http://iguye.com:41801'}
).json())

# requests.get(('http://httpbin.org/'),timeout = 5)