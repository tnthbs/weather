# weather
import requests,re

res = requests.get('http://www.weather.com.cn/weather1d/101280601.shtml')
text = res.content.decode()   #get content and decode from bytes

#get the string containing info
textRegx = re.compile(r'id="hidden_title" value=".*/>')
weather = textRegx.search(text).group() #get the string containing info

#replace the unneeded words with ''
weatherRegx = re.compile(r'id="hidden_title" value="|" />')
weather = weatherRegx.sub('',weather)

print('深圳 '+ weather)
