# weather
import requests,re,bs4
res = requests.get('http://www.weather.com.cn/weather1d/101280601.shtml')
res.raise_for_status()
res.encoding = 'UTF-8'
soup = bs4.BeautifulSoup(res.text,'lxml')
weather = soup.find_all(id="hidden_title")[0]
weatherRegx = re.compile(r'<input id="hidden_title" type="hidden" value="|"/>')
weather = weatherRegx.sub('',str(weather))


print('深圳 '+ weather)
