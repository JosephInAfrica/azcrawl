#!/usr/bin/env python
# encoding=utf-8
# decoding=utf-8
import csv
import codecs

class agent(object):
	def __init__(self,name='',email='',title='',mobile=''):
		self.name=name
		self.email=email
		self.title=title
		self.mobile=mobile


def sort():

	f=codecs.open('thailand.txt','r','utf-8')

	prefixes=['name','title','email','address','mobile']
	current=None
	g=open('thailand1.csv','w')
	writer=csv.writer(g)

	for l in f.readlines():
		l=l.replace(u'\u2019','')
		l=l.replace(':',' ')
		m=l.strip().split()
		if len(m)>1:
			if m[0] and m[0].lower() == u'name':
				current=agent(name=' '.join(m[1:]))
				print ('%s,%s added')%(m[0],' '.join(m[1:]))
				
			elif m[0].lower() =='email':
				if current is not None:
					current.email=' '.join(m[1:])
					try:
						print (current.name,current.email,current.title,current.mobile)
						writer.writerow([current.name,current.email,current.title,current.mobile])
						
					except:
						print ('not Wriiten',current.email)
					current=None
					
					try:
						print ('concluded')
					except:
						pass
			elif m[0].lower() in prefixes:
				if current is not None:
					setattr(current,m[0].lower(),' '.join(m[1:]))
				try:
					print ('%s,%s written')%(m[0],' '.join(m[1:]))
				except:
					pass
	g.close()
sort()
def readagents():
    new=[]
    f=open('indiawca.txt','r')
    for l in f.readlines():
        s=l.strip()
        if s is not '':
            print ("%s added"%s)
            new.append(s)
    with open('newindia.txt','w') as w:
        w.write('\n'.join(new))

