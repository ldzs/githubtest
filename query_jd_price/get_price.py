import requests
from bs4 import BeautifulSoup
import re


def 获取网址():
    url="https://item.jd.com/100007308631.html/"
    return url

def 获取skuId(url):
    skuId=url[20:]
    skuId=skuId[0:skuId.index(".")]
    skuId="J_"+skuId
    print(skuId)
    return skuId
    
def 查询价格(skuId):
    apiUrl="https://p.3.cn/prices/mgets?"
    r=requests.get(apiUrl,params={"skuId":skuId})
    print(r.text)
        
def main():
    url=获取网址()
    skuId=获取skuId(url)
    查询价格(skuId)


main()
