from fake_useragent import UserAgent
import requests
proxies = {
'http':'http://39.102.211.64:8008'
}
r = requests.get("http://httpbin.org/get",headers={'User-Agent':UserAgent().random},proxies=proxies)
if r.status_code == 200:
    print(r.text)