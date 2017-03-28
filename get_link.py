import requests
import os
from flask import Flask
from flask_script import Manager,Shell
from flask_sqlalchemy import SQLAlchemy

from bs4 import BeautifulSoup
import re
import csv
import codecs

def get_content(url):
	req=requests.get(url,timeout=2000)
	return req._content

def get_news_soup(url):
	req=requests.get(url,timeout=2000)
	soup=BeautifulSoup(req._content,'html.parser')
	news=soup.find('div',class_='featured_news_wrap')
	return news

def get_text(url):
	return get_soup(url).get_text()

def raw_treat(url,class_):
	soup=get_soup(url)
	item=soup.find_all('div',class_=class_)
	return item[0].get_text().strip()

def get_agent_links(url):
	agent_reg=re.compile(u"(listing\.html\?id=.*[1-9]+)")
	content=get_content(url).decode('utf-8')
	items=re.findall(agent_reg,content)
	return ['http://www.azfreight.com/'+ item for item in items]

def save_links(file_name,url):
	with open(file_name,'wb') as file:
		file.write('\n'.join(get_agent_links(url)).encode('utf-8'))

def read_links(file_name):
	with open(file_name,'r') as file:
		lines=file.readlines()
		return lines


if __name__=='__main__':
	save_links('indiaazlinks.txt','http://www.azfreight.com/search_results_directory.htm?comp_name=Company+Name&facility=-1&type_iata=0&products=0&geographic_location=1&country=India&location=-1&state=-1&criteria=Keywords&which_order=country&x=141&y=7')