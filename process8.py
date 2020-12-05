from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.error import HTTPError
import datetime
import random
import re
random.seed(datetime.datetime.now())
def getLinks(articleUrl):
    try:
        html = urlopen("http://en.wikipedia.org"+articleUrl)
        bsObj = BeautifulSoup(html,'html.parser')
    except HTTPError as e:
        return None
    else:
        return bsObj.find("div", {"id":"bodyContent"}).findAll("a",
                            href=re.compile("^(/wiki/)((?!:).)*$"))

links = getLinks("/wiki/Kevin_Bacon")
while len(links) > 0:
    newArticle = links[random.randint(0, len(links)-1)].attrs["href"]
    print(newArticle)
    links = getLinks(newArticle)