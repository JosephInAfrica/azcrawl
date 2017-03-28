import re
import os
import csv
class agent(object):
	def __init__(self,name,address,tel,fax,mobile,email,website,skype):
		self.name=name
		self.address=address
		self.tel=tel
		self.fax=fax
		self.mobile=mobile
		self.email=email
		self.website=website
		self.skype=skype



def clean(str):
	return re.sub(r'\s+',' ',str)


# print (csv.list_dialects())
# print (clean('\t\n\t\n    '))

# print ('\xe3')

url='http://www.azfreight.com/listing.html?id=c_35721'
# print ('\xe3'.encode('utf-8','ignore').decode('utf-8','ignore'))
basedir=os.path.abspath(os.path.dirname(__name__))
p=os.path.join(basedir,r'/','%s.txt'%'what')
no=re.findall(re.compile(r'id=([A-Za-z1-9-_]+)'),url)[0]
basedir=os.path.abspath(os.path.dirname(__name__))
print (p)
print (no)

print (basedir)