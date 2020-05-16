import requests
from bs4 import BeautifulSoup
array = ['title','body','url']
class Content:
    def __init__(self, url, title, body):
        self.url = url
        self.title = title
        self.body = body


def getPage(url):
    req = requests.get(url)
    return BeautifulSoup(req.text, 'html.parser')


def scrapeBitcoinWords(url):
    bs = getPage(url)
    title = bs.find('h1')
    body = bs.select('div')
    return Content(url, title, body)

def scrapeITWords(url):
    bs = getPage(url)
    title = bs.find('h1')
    body = bs.find('div')
    return Content(url, title, body)


def printText(content):
    f = open('test2.txt','a')
    f.write(str(content.url))
    f.write(str(content.title))
    f.close()
# IT用語
url = 'http://e-words.jp/p/s-ranking.html'
content = scrapeITWords(url)
printText(content)

# print('Title: {}'.format(content.title))
# print('URL: {}\n'.format(content.url))
# print(content.body)

url = 'https://bitcoin.dmm.com/glossary'
content = scrapeBitcoinWords(url)
printText(content)

# print('Title: {}'.format(content.title))
# print('URL: {}\n'.format(content.url))
# print(content.body)