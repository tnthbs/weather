from lxml import etree
import requests
res = requests.get('http://www.weather.com.cn/weather1d/101280601.shtml')
res.raise_for_status()
res.encoding = 'UTF-8'
selector = etree.HTML(res.content)  #res.content对象才为HTML源码
weather1 = selector.xpath('//*[@id="hidden_title"]/@value')
print('深圳 '+ weather1[0])
