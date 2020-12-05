from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup


try:
    html = urlopen("http://www.pythonscraping.com/pages/page1.html")
except HTTPError as e:
    print(e)
    if html is None:
        print("URL is not found")
    else:
        # 程序继续
        pass
else:
    # 程序继续。注意：如果你已经在上面异常捕捉那一段代码里返回或中断（break），
    # 那么就不需要使用else语句了，这段代码也不会执行
    pass