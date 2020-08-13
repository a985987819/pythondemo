import requests
from lxml import etree

proxies = {
    'https': 'https://127.0.0.1:1080',
    'http': 'http://127.0.0.1:1080'
}

# 自定义headers请求
#
# ua = 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1'
# headers = {'User-agent':ua}






r = requests.get('https://twitter.com/LynnChe93915556',proxies = proxies)

data = r.text
# print(data)
html = etree.HTML(data)
# html_data = html.xpath('//span[@class="css-901oao css-16my406 r-1qd0xha r-ad9z0x r-bcqeeo r-qvutc0"]/text()')
# html_data = html.xpath('//span[@class="css-901oao css-16my406 r-1re7ezh r-4qtqp9 r-1qd0xha r-ad9z0x r-zso239 r-bcqeeo r-qvutc0"]/text()')
result = etree.tostring(html)

# html_data = html.xpath('/html/body/div/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div/div[1]/div/div[3]/div/div[1]/span')
# html_data = html.xpath('//*[@id="react-root"]/div')
# html_data = html.xpath('/html/body/div/div/div/div[2]/div/div/div/div[1]/div/div[2]/div/div/div[1]/div/div[3]/div/div[1]/span')
html_data = html.xpath('//span[@class="css-901oao css-16my406 r-1qd0xha r-ad9z0x r-bcqeeo r-qvutc0"]')



# print(result.decode('utf-8'))
print(html_data)
print(r.status_code, r.reason)



# r = requests.post('http://www.baidu.com',data = {'a:''1'})