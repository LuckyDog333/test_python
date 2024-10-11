import urllib.request
from bs4 import BeautifulSoup
h = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36 Edg/128.0.0.0 "
}
dui = urllib.request.Request("https://movie.douban.com/top250", headers=h)
r = urllib.request.urlopen(dui)

html_doc = r.read().decode()
soup = BeautifulSoup(html_doc, 'html.parser')
lis = soup.find_all("div", class_="item")

for li in lis:
    print(li)
    print("*"*50)