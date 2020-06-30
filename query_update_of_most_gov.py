import requests
from bs4 import BeautifulSoup
import re


def 获取网址():
    return "https://service.most.gov.cn/kjjh_tztg_all/"

def 获取查询文本():
    return "制造"

def 处理网页(url):
    r=requests.get(url)
    demo=r.text.encode(r.encoding).decode('utf-8')
    soup=BeautifulSoup(demo,"html.parser")

    [s.extract() for s in soup('script')]

    return soup

def 输出查询结果(soup,text):
    i=0
    for item in  soup.findAll(string=re.compile(text)):
        i=i+1
        print("(",i,")",item.strip())
        
def main():
    url=获取网址()
    text=获取查询文本()
    soup=处理网页(url)
    输出查询结果(soup,text)


main()
