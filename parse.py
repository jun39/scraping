from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('https://pythonscraping.com/pages/page3.html')
bs =BeautifulSoup(html,'html.parser')

f = open('test2.txt','a')
for child in bs.find('table',{'id':'giftList'}).descendants:
    f.write(str(child))

f.close()