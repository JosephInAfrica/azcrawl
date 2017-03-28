import os
from flask import Flask, render_template, session, redirect, url_for
from flask_script import Manager, Shell
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import Required, Email
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail, Message

import time

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess string'
app.config['SQLALCHEMY_DATABASE_URI'] =\
    'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['MAIL_SERVER'] = 'smtp.sll.com.hk'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'tm7.szx@sll.com.hk'
app.config['MAIL_PASSWORD'] = 'joseph9012'
app.config['FLASKY_MAIL_SUBJECT_PREFIX'] = 'SuperLink'
app.config['FLASKY_MAIL_SENDER'] = 'Joseph SuperLink'
app.config['FLASKY_ADMIN'] = 'SuperLink'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

manager = Manager(app)
bootstrap = Bootstrap(app)
moment = Moment(app)
db = SQLAlchemy(app)
mail = Mail(app)


class Agent(db.Model):
    __tablename__ = 'agents'
    id = db.Column(db.Integer, primary_key=True)
    name= db.Column(db.String(64), unique=True, index=True)
    email = db.Column(db.String(128))
    country=db.Column(db.String(64))
    title=db.Column(db.String(64))
    mobile=db.Column(db.String(64))

    def __repr__(self):
        return '<User %r>' % self.name


class csvAgent(object):
    def __init__(self,name='',email='',title='',mobile=''):
        self.name=name
        self.email=email
        self.title=title
        self.mobile=mobile


def import_agents(name):
    import csv

    with open(name) as csvfile:
        reader=csv.reader(csvfile)
        for row in reader:

            print (row[0],row[1],row[2])

            agent=Agent(name=row[0],email=row[1],country=row[2])
            try:
                db.session.add(agent)
                db.session.commit()
                print ("%s added"%row[0])
            except:
                print ('%s not added'%row[0])
                db.session.rollback()

def readcsvandmail(filename='azamail.csv',topic='Shall we visit your office in middle of May--Superlink Logistics China',template='thailandvisit.html'):
    import csv

    with open(filename) as csvfile:
        reader=csv.reader(csvfile)
        record=open('Thailandrecord.txt','wb')
        # with mail.connect() as conn:
        for row in reader:

            agent,mail_addr=row[0],row[1]
            msg = Message(topic, sender='Joseph_SuperLink<tm7.szx@sll.com.hk>',
                  recipients=[mail_addr])

            msg.html = render_template(template, agent=agent)
            try:
                mail.send(msg)
                print ('mail sent to %s,%s'%(agent,mail_addr))
                record.write(('mail sent to %s,%s'%(agent,mail_addr)).encode('utf-8'))
            except:
                print ('Failure!mail not sentto %s,%s.'%(agent,mail_addr))
    

        record.close()


def mailto_agents():
    a=Agent.query.all()
    for i in a:

        group_mail('SuperLink',i.name,i.email)


def make_shell_context():
    return dict(app=app, db=db, Agent=Agent, import_agents=import_agents,mail=readcsvandmail)

manager.add_command("shell", Shell(make_context=make_shell_context))


if __name__ == '__main__':
    manager.run()
