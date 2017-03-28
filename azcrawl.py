from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import sys
import requests
from bs4 import BeautifulSoup
import re
import csv
import codecs
import os


basedir = os.path.abspath(os.path.dirname(__name__))
tmpdir = basedir + '\\tmp\\'

# class Agent(db.Model):
#     __tablename__ = 'agents'
#     id = db.Column(db.Integer, primary_key=True)
#     company= db.Column(db.String(128), unique=True, index=True)
#     email = db.Column(db.String(128))
#     # mobile=db.Column(db.String(128))
#     tel=db.Column(db.String(128))
#     web=db.Column(db.String(128))
#     fax=db.Column(db.String(128))
#     skype=db.Column(db.String(64))
#     # country=db.Column(db.String(64))
#     # group=db.Column(db.String(64))
#     def __repr__(self):
#         return '<User %r>' % self.company


def clean(str):
    return re.sub(r'\s+', ' ', str).encode('utf-8', 'ignore').decode('utf-8', 'ignore')


def get_content(url):
    req = requests.get(url, timeout=2000)
    return req._content


def get_news_soup(url):
    no = re.findall(re.compile(r'id=([A-Za-z1-9-_]+)'), url)[0]
    try:
        f = open(tmpdir + r'%s.txt' % no, 'r', encoding='utf-8')
        print('find saved info')
        soup = BeautifulSoup(f.read(), 'html.parser')
    except:
        req = requests.get(url, timeout=2000)
        print('request new info')
        with open(tmpdir + r'%s.txt' % no, 'w', encoding='utf-8') as f:
            f.write(req._content.decode('utf-8'))
        print('new info written')
        soup = BeautifulSoup(req._content, 'html.parser')
    news = soup.find('div', class_='featured_news_wrap')
    return news


def get_text(url):

    return get_soup(url).get_text()


def raw_treat(url, class_):
    soup = get_soup(url)
    item = soup.find_all('div', class_=class_)
    return item[0].get_text().strip()


def get_agent_links(url):
    agent_reg = re.compile(u"(listing\.html\?id=.*[1-9]+)")
    content = requests.get(url)._content.decode('utf-8')
    items = re.findall(agent_reg, content)
    return ['http://www.azfreight.com/' + item for item in items]


def save_links(file_name, url):
    with open(file_name, 'wb') as file:
        file.write('\n'.join(get_agent_links(url)).encode('utf-8'))


def read_links(file_name):
    with open(file_name, 'r') as file:
        lines = file.readlines()
        return lines


def crawl(csv_file, linkfile):
    # with open('thailandaz.txt','wb') as thailandaz:

    with open(csv_file, 'w', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile, dialect='excel')

        for url in read_links(linkfile):
            print('link parsing:%s' % url)
            row = parse(url)
            if url[1] is not '':
                # writer.writerow((','.join(parse(url))+'\n').encode('utf-8'))
                writer.writerow(parse(url))


def parse(url):
    soup = get_news_soup(url)
    # soup=BeautifulSoup(get_content(url),'html.parser')
    try:
        company_name = soup.find('div', class_='listing_info').find(
            'h2').get_text().strip('\n')
    except:
        company_name = 'NoName'
    # print (company_name)

    boxes = soup.find_all('div', class_='listing_info_box')

    box = soup.find('div', class_='listing_info')

    emailreg = re.compile(u'Email: (.*)')
    telreg = re.compile(u'Tel: (.*)')
    faxreg = re.compile(u'Fax: (.*)')
    websitereg = re.compile(u'Website: (.*)')
    skypereg = re.compile(u'Skype:(.*)')
    # if (len(boxes))==2:

    address = boxes[0].get_text().strip('\n')
    # print (address)

    eles = box.find_all('li')
    mail, tel, fax, web, skype = [], [], [], [], []
    try:
        for ele in eles:
            ele = ele.get_text()
            mail.append(''.join(re.findall(emailreg, ele)))
            tel.append(''.join(re.findall(telreg, ele)))
            web.append(''.join(re.findall(websitereg, ele)))
            fax.append(''.join(re.findall(faxreg, ele)))
            skype.append(''.join(re.findall(skypereg, ele)))
    except:
        pass
    mail, tel, fax, web, skype = ';'.join([t for t in mail if t is not '']), ';'.join(
        [t for t in tel if t is not '']), ''.join(fax), ''.join(web), ''.join(skype)
    print('name:%s\n' % company_name, 'email:%s\n' % mail, 'tel:%s\n' % tel, 'fax:%s\n' %
          fax, 'web:%s\n' % web, 'skype:%s\n' % skype, 'address:%s\n' % address)
    return [clean(company_name), clean(mail), clean(tel), clean(fax), clean(web), clean(skype), clean(address)]
    # return (company_name,mail)

if __name__ == '__main__':
    crawl(sys.argv[1], sys.argv[2])
    # save_links('azindialinks.txt', 'http://www.azfreight.com/search_results_directory.htm?which_directory=specific&geographic_location=1&criteria=&location=-1&facility=-1&country=India&x=54&y=11')
