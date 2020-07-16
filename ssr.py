import requests
from lxml import etree
url='https://github.com/freefq/free'
res=requests.get(url)
selector=etree.HTML(res.content)
content=selector.xpath('//article[@class="markdown-body entry-content container-lg"]/*/text()')

for x in content:
    print(x)
