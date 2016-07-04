
from flask_mail import Message
from threading import Thread
from . import mail
from flask import render_template,current_app


def send_async_email(app,msg):
    with app.app_context():
        mail.send(msg)

def send_email(subject,recipients,template,**kwargs):
    app = current_app._get_current_object()
    msg = Message(subject,recipients=recipients,sender='admin@xubiaosunny.net')
    msg.body = render_template(template+'.txt',**kwargs)
    msg.html = render_template(template+'.html',**kwargs)
    th = Thread(target=send_async_email,args=[app,msg])
    th.start()

    return th