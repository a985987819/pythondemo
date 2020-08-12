import requests

proxies = {
    'https': 'https://127.0.0.1:1080',
    'http': 'http://127.0.0.1:1080'
}

# 自定义headers请求
#
# ua = 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1'
# headers = {'User-agent':ua}


r = requests.get('https://twitter.com/LynnChe93915556',proxies = proxies)

print(r.status_code, r.reason)
print(r.text)


# r = requests.post('http://www.baidu.com',data = {'a:''1'})