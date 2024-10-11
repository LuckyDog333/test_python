import requests
proxies = {
        'http':'http://39.102.211.64:8008',
        # 'https':'https://23.226.117.85:8080',
}
h = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36 Edg/128.0.0.0 "
}
r = requests.get("http://httpbin.org/get", headers=h, proxies=proxies)
if r.status_code == 200:
    print(requests.get("https://movie.douban.com/top250", headers=h, proxies=proxies).text)