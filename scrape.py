from urllib.request import urlopen

html = urlopen('http://e-words.jp/p/i-kaa.html')
print(html.read())