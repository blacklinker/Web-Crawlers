from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.error import HTTPError
import re
pages = set()
def getLinks(pageUrl):
    global pages
    html = urlopen("http://en.wikipedia.org"+pageUrl)
    bsObj = BeautifulSoup(html,'html.parser')
    try:
        print(bsObj.h1.get_text())
    except HTTPError as e:
        print('cant find h')
    try:
        print(bsObj.find(id='mw-content-text').findAll('p')[0])
    except HTTPError as e:
        print("cant find p")
    try:
        print(bsObj.find(id='ca-edit').find('span').find('a').attrs['href'])
    except AttributeError:
        print("页面缺少一些属性！不过不用担心！")

    for link in bsObj.findAll("a", href=re.compile("^(/wiki/)")):
        if 'href' in link.attrs:
            if link.attrs['href'] not in pages:
            # 我们遇到了新页面
                newPage = link.attrs['href']
                print("----------------\n" + newPage)
                pages.add(newPage)
                getLinks(newPage)

getLinks("")
