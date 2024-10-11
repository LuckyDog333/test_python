from fake_useragent import UserAgent
import requests
proxies = {
'http':'http://153.101.67.170:9002'
}
data = {
    'name' : '张三',
    'age' : '13'
}
r = requests.post("http://httpbin.org/post",headers={'User-Agent':UserAgent().random},proxies = proxies, data=data)
if r.status_code == 200:
    print(r.text)