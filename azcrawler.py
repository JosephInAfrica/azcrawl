import requests
from bs4 import BeautifulSoup
import re
import csv
import codecs
# req=requests.get('http://www.azfreight.com/listing.html?id=c_20094',timeout=10)

# soup=BeautifulSoup(req._content,'html.parser')
# # print (req.__dir__())
# # print (req.raw)

def get_soup(url):
	req=requests.get(url,timeout=2000)
	soup=BeautifulSoup(req._content,'html.parser')
	return soup
def get_content(url):
	req=requests.get(url,timeout=2000)
	return req._content

def get_text(url):
	return get_soup(url).get_text()


def get_featured_news(url):
	return get_soup(url).find('div',class_='listing_info').get_text()



def raw_treat(url,class_):
	soup=get_soup(url)
	item=soup.find_all('div',class_=class_)
	return item[0].get_text().strip()


# item=soup.find_all('div',class_='listing_info')
# soup=BeautifulSoup(req,'html.parser')
# open('sp.txt','wb').write(item[0].get_text().strip().encode('utf-8'))

def get_agent_links(url):
	agent_reg=re.compile(u"(listing\.html\?id=.*[1-9]+)")
	content=get_content(url).decode('utf-8')
	items=re.findall(agent_reg,content)
	return ['http://www.azfreight.com/'+ item for item in items]

def save_links(file_name,url):
	with open(file_name,'wb') as file:
		file.write('\n'.join(get_agent_links(url)).encode('utf-8'))

# save_links('thailandAZlinks.txt','http://www.azfreight.com/search_results_directory.htm?comp_name=Company+Name&facility=-1&type_iata=0&products=0&geographic_location=1&country=Thailand&location=-1&state=-1&criteria=Keywords&which_order=country&x=148&y=8')

def read_links(file_name):
	with open(file_name,'r') as file:
		lines=file.readlines()
		return lines

class agent(object):
	def __init__(self,name='',address='',tel='',fax='',mobile='',email='',website='',skype=''):
		self.name=name
		self.address=address
		self.tel=tel
		self.fax=fax
		self.mobile=mobile
		self.email=email
		self.website=website
		self.skype=skype


def get_info(soup):
	soup=get_soup(url)
	soup.find('div',class_='listing_info').find('h2')


def get_agent(text):
	emailreg=re.compile(u'Email: (.*)')
	telreg=re.compile(u'Tel: (.*)')
	faxreg=re.compile(u'Fax: (.*)')
	websitereg=re.compile(u'Website: (.*)')
	skypereg=re.compile(u'Skype: (.*)')
	
	lines=[i.strip() for i in text.split('\n\n') if len(i)>0]
	
	newagent=agent()
	try:
		newagent.name=lines[0].split('\n')[0]
		newagent.address=lines[1].replace('\n','\t')
		newagent.email=','.join(re.findall(emailreg,lines[2]))
		newagent.tel=','.join(re.findall(telreg,lines[2]))
		newagent.fax=','.join(re.findall(faxreg,lines[2]))
		newagent.website=','.join(re.findall(websitereg,lines[2]))
		newagent.skype=','.join(re.findall(skypereg,lines[2]))
	except:
		pass

	# print (newagent.name)
	# print (newagent.address)
	# print(newagent.email)
	# print(newagent.tel)
	# print(newagent.fax)
	# print(newagent.website)

	print ('name:%s\n'%newagent.name,'address:%s\n'%newagent.address,'email:%s\n'%newagent.email,'tel:%s\n'%newagent.tel,'fax:%s\n'%newagent.fax,'website:%s\n'%newagent.website)
	print ('row written')
	return [newagent.name,newagent.address,newagent.email,newagent.tel,newagent.fax,newagent.website]
def getraw():
	with open('thailandazraw.txt','wb') as file:
		
		for link in read_links('thailandazlinks.txt'):
			link=link.replace('\n','')
			print ('link to crawl:%s\n'%link)
			text=get_featured_news(link)
			print (text+'\n')
			file.write(text.encode('utf-8'))
			print ('row written')	

# getraw()
def get_thailand():
	with open('thailandaz.txt','wb') as file:
		
		for link in read_links('thailandazlinks.txt'):
			link=link.replace('\n','')
			print ('link to crawl:%s\n'%link)
			text=get_featured_news(link)
			agent_info=get_agent(text)
			print ('agent_info:%s\n'%agent_info)
			file.write((','.join(agent_info)+'\n').encode('utf-8'))
			print ('row written')



# get_thailand('http://www.azfreight.com/search_results_directory.htm?comp_name=Company+Name&facility=-1&type_iata=0&products=0&geographic_location=1&country=Thailand&location=-1&state=-1&criteria=Keywords&which_order=country&x=148&y=8')

# print (get_agent((get_featured_news('http://www.azfreight.com/listing.html?id=c_21317'))))
# get_thailand()
