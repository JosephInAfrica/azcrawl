from bs4 import BeautifulSoup

def openfile(file):
	f=open(file,'r')
	return f.read()

soup=BeautifulSoup(openfile('links.html'),'html.parser')

print soup.find_all('a')


