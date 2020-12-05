# import pymysql
# conn = pymysql.connect(host='127.0.0.1', unix_socket='/tmp/mysql.sock',
# user='root', passwd=None, db='mysql')
# cur = conn.cursor()
# cur.execute("USE scraping")
# cur.execute("SELECT * FROM pages WHERE id=1")
# print(cur.fetchone())
# cur.close()
# conn.close()


from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import datetime
import random
import pymysql

conn = pymysql.connect(host='127.0.0.1', unix_socket='/tmp/mysql.sock',
user='root', passwd=None, db='mysql', charset='utf8')
cur = conn.cursor()
cur.execute("USE scraping")
random.seed(datetime.datetime.now())
def store(title, content):
    cur.execute("INSERT INTO pages (title, content) VALUES (\"%s\",\"%s\")", (title, content))
    cur.connection.commit()

def getLinks(articleUrl):
    html = urlopen("http://en.wikipedia.org"+articleUrl)
    bsObj = BeautifulSoup(html,'html.parser')
    title = bsObj.find("h1").get_text()
    content = bsObj.find("div", {"id":"mw-content-text"}).find("p").get_text()
    store(title, content)
    return bsObj.find("div", {"id":"bodyContent"}).findAll("a",
                    href=re.compile("^(/wiki/)((?!:).)*$"))

links = getLinks("/wiki/Kevin_Bacon")
try:
    while len(links) > 0:
        newArticle = links[random.randint(0, len(links)-1)].attrs["href"]
        print(newArticle)
        links = getLinks(newArticle)
finally:
    cur.close()
    conn.close()


# Unicode：
# ALTER DATABASE scraping CHARACTER SET = utf8mb4 COLLATE = utf8mb4_unicode_ci;
# ALTER TABLE pages CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
# ALTER TABLE pages CHANGE title title VARCHAR(200) CHARACTER SET utf8mb4 COLLATE
# utf8mb4_unicode_ci;
# ALTER TABLE pages CHANGE content content VARCHAR(10000) CHARACTER SET utf8mb4 CO
# LLATE utf8mb4_unicode_ci;
# 这四行语句改变的内容有：数据库、数据表，以及两个字段的默认编码都从utf8mb4
# （严格说来也属于Unicode，但是对大多数Unicode 字符的支持都非常不好）转变成了
# utf8mb4_unicode_ci。