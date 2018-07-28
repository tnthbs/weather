# weather
import requests,bs4

res = requests.get('http://www.weather.com.cn/weather1d/101280601.shtml')
text = res.content.decode()   #get content and decode from bytes
bs = bs4.BeautifulSoup(text,'lxml')
content = bs.find(id="hidden_title")['value']   #content is include in 
title = bs.title.string # get the title of city 
print(title,content,sep='\n')
