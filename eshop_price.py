import requests
import json
from lxml import etree

html = requests.get('https://eshop-prices.com/prices?currency=CNY')
etree_html = etree.HTML(html.text)
# tr = etree_html.xpath('//*[@class="prices"]/table/tbody/tr[%s]' % (i))

def getPrices(limit = 1):
  offset = 1
  result = []
  
  def getData(offset, limit):
    print(limit * offset, limit * (offset + 1))
    for i in range(limit * offset, limit * (offset + 1)):
      print(i)
      title = etree_html.xpath('//*[@class="prices"]/table/tbody/tr[%s]/th[1]/a[1]/text()' % (i))[0]
      prices = etree_html.xpath('//*[@class="prices"]/table/tbody/tr[%s]/td/text()' % (i))
      item = {
        'title': title,
        'prices': prices
      }
      result.append(item)
    
  getData(offset, limit)
    # result.append(item)

    # print(content[i], etree_html.xpath('//*[@class="prices"]/table/tbody/tr[%s]/td/text()' % (i)))
  # print(result)
  with open('switch_all_game_title.json','w') as file:
    file.write(json.dumps(result))