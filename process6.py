from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

html = urlopen('http://www.pythonscraping.com/pages/page3.html')

bsObj = BeautifulSoup(html,'html.parser')

images = bsObj.find_all('img',{'src': re.compile('\.\./img/gifts/img\d{1}\.jpg')})

a = bsObj.find_all('tr')

for image in images:
#     print(image['src'])
    if 'src' in image.attrs:
        print(image.attrs["src"])


# 获得标签属性
# for i in a:
#     print(i.attrs)


# images = bsObj.findAll("img",{"src":re.compile("\.\.\/img\/gifts/img.*\.jpg")})
# for image in images:
#     print(image["src"])


# 下面的代码就是获取有两个属性的标签:
# bsObj.findAll(lambda tag: len(tag.attrs) == 2)
