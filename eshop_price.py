import requests
from lxml import etree

def getPrices():
  html = requests.get("https://blog.csdn.net/it_xf?viewmode=contents")
  
  etree_html = etree.HTML(html.text)
  content = etree_html.xpath('//*[@id="mainBox"]/main/div[2]/div[1]/h4/a/text()')
  for each in content:
    print(each)