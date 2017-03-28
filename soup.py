from bs4 import BeautifulSoup
import string
cat=open('cater.html').read()

soup=BeautifulSoup(cat,'html.parser')

t=soup.get_text()

l=soup.find_all('td')

# print soup.title
# print soup.prettify()
# print soup.find_all('td')
# print soup.find_all(text='')

# print l
# l= t.split(u'\n')
# print t.strip()
