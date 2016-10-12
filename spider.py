# -*-coding: utf-8 -*-
from urllib.request import urlopen, FancyURLopener
from bs4 import BeautifulSoup
import requests
import re
import time


def getHTML(url):
    r = requests.get(url, headers=headers)
    with open('html.html', 'w', encoding='utf-8') as f:
        f.write(r.text)


def getURL(html):
    url_lt = []
    with open('html.html', encoding='utf-8') as f:
        htmlfile = f.read()
    bsObj = BeautifulSoup(htmlfile, 'lxml')
    ltObj = bsObj.findAll("img", {"src": re.compile(r"http:.*\.jpg")})
    for item in ltObj:
        url_lt.append(item['src'])
    return url_lt


def download(ltobj):
    length = len(ltobj)
    for i in range(length):
        name = str(i) + '.jpg'
        print(ltobj[i])
        with open(name, 'wb') as f:
            pic = myopener.open(ltobj[i])
            try:
                pic_data = pic.read()
            except ValueError:
                continue
            f.write(pic_data)
        print('Have downloaded %dth' % i)
        time.sleep(3)


def getFile(url):
    pass


def genURLs(url, total=1):
    urls = [url]
    if total == 1:
        return urls 
    for i in range(2, total+1):
        nxturl = url + 'index' + str(i) + '.html'
        urls.append(nxturl)
    return urls


if __name__ == "__main__":
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6',
        'Connection': 'keep-alive',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko'
    }

    HTML = r"F:\IdeaProject\spider\spider\html.html"
    class MyOpener(FancyURLopener):
        version = headers['User-Agent']
    myopener = MyOpener()

    objURLs = []
    url = input("Please input url: ")
    total = int(input("How many pages: "))
    URLs = genURLs(url, total)
    for URL in URLs:
        getHTML(URL)
        url_lt = getURL(HTML)
        objURLs.extend(url_lt)
    download(objURLs)

    
    # download(getURL(html))
    # url = input("Please input url: ")
    # urls = genURLs(url, 3)
    # for item in urls:
    #     print(item)