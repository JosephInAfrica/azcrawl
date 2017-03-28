#!/usr/bin/env python
# encoding=utf-8

import requests
from bs4 import BeautifulSoup

DOWNLOAD_URL = []

def get_url():
	pass

def download_page(url,file='agents.html'):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36'
    }
    data = requests.get(url, headers=headers).content
    try:
    	f=open(file,'w')
    	f.write(data)
    	f.close()
    finally:
    	print 'done'


def main():
    print download_page('http://www.wcaworld.com/eng/directory.asp?searchby=city&orderby=city&name=IN&statecity=&city=&keyword=&allnet=yes&n=1&n=2&n=3&n=4&n=61&n=98')


if __name__ == '__main__':
    main()
