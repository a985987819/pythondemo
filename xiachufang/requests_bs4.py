import os

from bs4 import BeautifulSoup
import requests
from urllib.parse import urlparse


#模拟浏览器访问
ua = 'Mozilla/5.0 ' \
     '(Windows NT 10.0; Win64; x64) ' \
     'AppleWebKit/537.36 (KHTML, like Gecko) ' \
     'Chrome/80.0.3987.116 Safari/537.36'
header = {'User-Agent': ua}



r = requests.get('http://www.xiachufang.com/',headers = header)

soup = BeautifulSoup(r.text,'lxml')
soup.select('img')
# print(soup.select('img'))

img_list = []
for img in soup.select('img'):
    if img.has_attr('data-src'):
        img_list.append(img.attrs['data-src'])
    else:
        img_list.append(img.attrs['src'])


# 初始化下载文件目录
image_dir = os.path.join(os.curdir,'images')


for img in img_list:
    o = urlparse(img)
    filename = o.path[1:].split('@')[0]
    filepath = os.path.join(image_dir,filename)

# 如无目录则创建
    if not os.path.isdir(os.path.dirname(filepath)):
        os.mkdir(os.path.dirname(filepath))

    url = '%s://%s/%s' %(o.scheme,o.netloc,filename)

    # print(filepath)
    # print(filename)

    print(url)

    resp = requests.get(url)
    with open(filepath,'wb') as f:
        for chunk in resp.iter_content(1024):
            f.write(chunk)