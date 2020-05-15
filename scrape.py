from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('http://e-words.jp/p/i-kaa.html')
bs = BeautifulSoup(html,'html.parser')
f = open('test.txt','w')
f.write(str(bs.div))
f.close()