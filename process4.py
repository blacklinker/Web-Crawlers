from urllib.request import urlopen
from bs4 import BeautifulSoup

http = urlopen('http://www.pythonscraping.com/pages/warandpeace.html')

bsObj = BeautifulSoup(http, 'html.parser')


# nameList = bsObj.find_all(text='the prince')
# print(len(nameList))



# nameList = bsObj.find_all('span',{'class': {'green','red'}})
# for name in nameList:
#     print(name.get_text())
#     print()

# allText = bsObj.findAll(id="text")
# print(allText[0].get_text())

# texts = bsObj.find_all(class_ = 'green')

texts = bsObj.div.span

for text in texts:
    print(text)




