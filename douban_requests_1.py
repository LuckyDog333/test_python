<<<<<<< HEAD
import requests
import re
import pymysql.cursors
from fake_useragent import UserAgent
# 数据库id
id_sql = 0
# 控制翻页变量
x = 0
proxies = {
'http':'http://153.101.67.170:9002'
}
#循环翻页爬取10页
for i in range(0, 11):
    #翻页累加25
    url = "https://movie.douban.com/top250?start=" + str(x) +"&filter="
    x = x + 25
    #连接数据库
    connection = pymysql.connect(host='localhost',
                                 user='root',
                                 password='123456',
                                 database='spider_douban1',
                                 cursorclass=pymysql.cursors.DictCursor)
    #获取网页资源
    rep = requests.get(url,headers={'User-Agent':UserAgent().random},proxies=proxies)
    #转为text格式
    page_content = rep.text
    #用捕获组正则表达式
    obj = re.compile(r'.*?<li>.*?<img width="100" alt="(?P<name>.*?)"'
                            r'.*?src="(?P<image_url>.*?)"'
                            r'.*?<span class="other">&nbsp;/&nbsp;(?P<other_name>.*?)</span>'
                            r'.*?<div class="bd">.*?<p class="">(?P<director>.*?)<br>'
                            r'(?P<year>.*?)&nbsp;'
                            r'/&nbsp;(?P<country>.*?)&nbsp;'
                            r'/&nbsp;(?P<style>.*?)</p>'
                            r'.*?<span class="rating_num" property="v:average">(?P<score>.*?)</span>'
                            r'.*?<span>(?P<review>.*?)</span>'
                            r'.*?</div>(?P<one_review>.*?)</div>'
                            ,re.S)
    #返回一个迭代器
    items = obj.finditer(page_content)
    #开始每一页的爬取
    with connection:
        for item in items:
            #数据处理
            id_sql = id_sql + 1
            name = item.group('name')
            image_url = item.group('image_url')
            other_name = item.group('other_name')
            director0 = item.group('director').strip()
            p_d = r'导演:(.*?)&nbsp;'
            p_p = r'主演:(.*?)$'
            #一些特殊情况,比如没有演员，非常恶心
            try:
                director = re.search(p_d, director0).group(1)
            except AttributeError:
                p_d = r'导演:(.*?)$'
                director = re.search(p_d, director0).group(1)
            try:
                performer = re.search(p_p, director0).group(1)
            except AttributeError:
                performer = ''
            year = item.group('year').strip()
            country = item.group('country')
            style = item.group('style').strip()
            review = item.group('review')
            one_review0 = item.group('one_review').strip()
            pattern = r'<span class="inq">(.*?)</span>'
            #没有评语的电影
            try:
                one_review = re.search(pattern, one_review0).group(1)
            except AttributeError:
                one_review = ''
            score = item.group('score')
            #插入数据库
            with connection.cursor() as cursor:
                    sql = "INSERT INTO `movie_info` (`id`, `name`, `other_name`, `year`, `country`, `style`, `director`, `performer`, `score`, `review`, `one_review`, `image_url`) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
                    cursor.execute(sql, (id_sql, name, other_name, year, country, style, director, performer, score, review, one_review, image_url))
        connection.commit()
=======
import requests
import re
import pymysql.cursors
from fake_useragent import UserAgent
# 数据库id
id_sql = 0
# 控制翻页变量
x = 0
proxies = {
'http':'http://153.101.67.170:9002'
}
#循环翻页爬取10页
for i in range(0, 11):
    #翻页累加25
    url = "https://movie.douban.com/top250?start=" + str(x) +"&filter="
    x = x + 25
    #连接数据库
    connection = pymysql.connect(host='localhost',
                                 user='root',
                                 password='123456',
                                 database='spider_douban1',
                                 cursorclass=pymysql.cursors.DictCursor)
    #获取网页资源
    rep = requests.get(url,headers={'User-Agent':UserAgent().random},proxies=proxies)
    #转为text格式
    page_content = rep.text
    #用捕获组正则表达式
    obj = re.compile(r'.*?<li>.*?<img width="100" alt="(?P<name>.*?)"'
                            r'.*?src="(?P<image_url>.*?)"'
                            r'.*?<span class="other">&nbsp;/&nbsp;(?P<other_name>.*?)</span>'
                            r'.*?<div class="bd">.*?<p class="">(?P<director>.*?)<br>'
                            r'(?P<year>.*?)&nbsp;'
                            r'/&nbsp;(?P<country>.*?)&nbsp;'
                            r'/&nbsp;(?P<style>.*?)</p>'
                            r'.*?<span class="rating_num" property="v:average">(?P<score>.*?)</span>'
                            r'.*?<span>(?P<review>.*?)</span>'
                            r'.*?</div>(?P<one_review>.*?)</div>'
                            ,re.S)
    #返回一个迭代器
    items = obj.finditer(page_content)
    #开始每一页的爬取
    with connection:
        for item in items:
            #数据处理
            id_sql = id_sql + 1
            name = item.group('name')
            image_url = item.group('image_url')
            other_name = item.group('other_name')
            director0 = item.group('director').strip()
            p_d = r'导演:(.*?)&nbsp;'
            p_p = r'主演:(.*?)$'
            #一些特殊情况,比如没有演员，非常恶心
            try:
                director = re.search(p_d, director0).group(1)
            except AttributeError:
                p_d = r'导演:(.*?)$'
                director = re.search(p_d, director0).group(1)
            try:
                performer = re.search(p_p, director0).group(1)
            except AttributeError:
                performer = ''
            year = item.group('year').strip()
            country = item.group('country')
            style = item.group('style').strip()
            review = item.group('review')
            one_review0 = item.group('one_review').strip()
            pattern = r'<span class="inq">(.*?)</span>'
            #没有评语的电影
            try:
                one_review = re.search(pattern, one_review0).group(1)
            except AttributeError:
                one_review = ''
            score = item.group('score')
            #插入数据库
            with connection.cursor() as cursor:
                    sql = "INSERT INTO `movie_info` (`id`, `name`, `other_name`, `year`, `country`, `style`, `director`, `performer`, `score`, `review`, `one_review`, `image_url`) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
                    cursor.execute(sql, (id_sql, name, other_name, year, country, style, director, performer, score, review, one_review, image_url))
        connection.commit()
>>>>>>> ea41d79f6e47bd025cf10c85ff124ac35b195b42
