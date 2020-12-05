from bs4 import BeautifulSoup
from urllib.request import urlopen
import re
import pymysql
conn = pymysql.connect(host='127.0.0.1', unix_socket='/tmp/mysql.sock',user=
                        'root', passwd=None, db='mysql', charset='utf8')
cur = conn.cursor()
cur.execute("USE wikipedia")
def insertPageIfNotExists(url):
    cur.execute("SELECT * FROM pages WHERE url = %s", (url))
    if cur.rowcount == 0:
        cur.execute("INSERT INTO pages (url) VALUES (%s)", (url))
        conn.commit()
        return cur.lastrowid
    else:
        return cur.fetchone()[0]
def insertLink(fromPageId, toPageId):
    cur.execute("SELECT * FROM links WHERE fromPageId = %s AND toPageId = %s",
    (int(fromPageId), int(toPageId)))
    if cur.rowcount == 0:
        cur.execute("INSERT INTO links (fromPageId, toPageId) VALUES (%s, %s)",
        (int(fromPageId), int(toPageId)))
        conn.commit()
pages = set()
def getLinks(pageUrl, recursionLevel):
    global pages
    if recursionLevel > 4:
        return;
    pageId = insertPageIfNotExists(pageUrl)
    html = urlopen("http://en.wikipedia.org"+pageUrl)
    bsObj = BeautifulSoup(html,'html.parser')
    for link in bsObj.findAll("a",
                              href=re.compile("^(/wiki/)((?!:).)*$")):
                                insertLink(pageId,
                                    insertPageIfNotExists(link.attrs['href']))
    if link.attrs['href'] not in pages:
        # 遇到一个新页面，加入集合并搜索里面的词条链接
        newPage = link.attrs['href']
        pages.add(newPage)
        getLinks(newPage, recursionLevel+1)
getLinks("/wiki/Kevin_Bacon", 0)
cur.close()
conn.close()

#SMTP



# 这个程序每小时检查一次https://isitchristmas.com/ 网站（根据日期判断当天是不是圣诞
# 节）。如果页面上的信息不是“NO”（中国用户在网站页面上看到的“NO”在源代码里是
# <noscript> 不是</noscript>），就会给你发一封邮件，告诉你圣诞节到了。
# 虽然这个程序看起来并没有墙上的挂历有用，但是稍作修改就可以做很多有用的事情。它
# 可以发送网站访问失败、应用测试失败的异常情况，也可以在Amazon 网站上出现了一款
# 卖到断货的畅销品时通知你——这些都是挂历做不到的事情。
# import smtplib
# from email.mime.text import MIMEText
# from bs4 import BeautifulSoup
# from urllib.request import urlopen
# import time
# def sendMail(subject, body):
#     msg = MIMEText(body)
#     msg['Subject'] = subject
#     msg['From'] = "christmas_alerts@pythonscraping.com"
#     msg['To'] = "ryan@pythonscraping.com"
#     s = smtplib.SMTP('localhost')
#     s.send_message(msg)
#     s.quit()
#     bsObj = BeautifulSoup(urlopen("https://isitchristmas.com/"))
#     while (bsObj.find("a", {"id": "answer"}).attrs['title'] == "NO"):
#         print("It is not Christmas yet.")
#     time.sleep(3600)
#     bsObj = BeautifulSoup(urlopen("https://isitchristmas.com/"))
#     sendMail("It's Christmas!",
#              "According to http://itischristmas.com, it is Christmas!")
#