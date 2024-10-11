import urllib.request

import ddddocr
from fake_useragent import UserAgent
import requests
import re
h = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36 Edg/128.0.0.0 "
}
proxies = {
'http':'http://153.101.67.170:9002'
}
s = requests.Session()
r = requests.get("https://www.nowapi.com/?app=account.login",headers={'User-Agent':UserAgent().random},proxies = proxies)
page_content = r.text
obj = re.compile(r'.*?<img id="authCodeImg" src="(?P<url>.*?)"')
url = obj.findall(page_content)[0]
print(url)
# print(r.text)
# # print(s.cookies.keys())
# for item in s.cookies.iteritems():
#     print(item[0] + ":" + item[1])
response = s.get(url,headers={'User-Agent':UserAgent().random},proxies=proxies)
if response.status_code == 200:
    with open('ex.jpg','wb') as f:
        f.write(response.content)
else:
    print(f"下载失败，状态码：{response.status_code}")
ocr = ddddocr.DdddOcr()
image = open("ex.jpg","rb").read()
result = ocr.classification(image)
print(result)

data = {
    'username' : 'kkluv',
    'passwd' : '123456',
    'authcode' : result,
    'app' : 'accountr.aja_login'
}
r = requests.post("https://www.nowapi.com/index.php?ajax=1",headers=h,proxies = proxies,data=data)
print(r.text)