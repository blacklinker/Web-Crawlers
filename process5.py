from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('http://www.pythonscraping.com/pages/page3.html')
bsObj = BeautifulSoup(html, 'html.parser')


# 子标签
# for child in bsObj.find('table', {'id': 'giftList'}).children:
#     print(child)

# 后代标签
# for descendant in bsObj.find('table', {'id': 'giftList'}).descendants:
#     print(descendant)

# # 兄弟标签
# for sibling in bsObj.find('table', {'id': 'giftList'}).tr.next_siblings: #previous_siblings
#     print(sibling)
# previous_sibling 和 next_sibling 返回单个

# 父类标签
print(bsObj.find("img",{"src":"../img/gifts/img1.jpg"
}).parent.previous_sibling.get_text())