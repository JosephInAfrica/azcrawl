import requests
from bs4 import BeautifulSoup

headers={'user-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:51.0) Gecko/20100101 Firefox/51.0'}
# cookies=dict(CFID=2585364, CFTOKEN=12544076, OAID=40a050fd28f2b3bb71a035a00eec1ca6, __utma=129949660.796186656.1489025315.1489025315.1489025315.1, __utmb=129949660.4.10.1489025315, __utmc=129949660, __utmz=129949660.1489025315.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none), PHPSESSID=1v8hahlfrfa7s7iim6m8js2o01, member_id=58c0bb707892c)
r=requests.get('http://www.azfreight.com/listing.html?id=c_20094')
print r.headers

# print r.text