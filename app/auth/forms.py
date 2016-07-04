#-*-coding:utf-8-*-
from flask_wtf import Form
from wtforms import StringField,PasswordField,BooleanField,SubmitField
from wtforms.validators import Required,Length,Email,Regexp,EqualTo

class registerForm(Form):
    email = StringField(u'邮箱',validators = [Required(),Length(1,64),Email()])
    username = StringField(u'用户名',validators = [Required(),Length(1,64),Regexp('^[A-Za-z][A-Za-z0-9_.]*$', 0,
                                                                                  u'用户名必须只包含字母，数字或下划线')])
    password = PasswordField(u'密码',validators = [Required(),Length(1,64),Regexp('^[A-Za-z][A-Za-z0-9_.]*$', 0,
                                                                                  u'密码必须只包含字母，数字或下划线')])
    password_confirm = PasswordField(u'确认密码',validators = [EqualTo('password', message=u'密码不匹配.')])
    submit = SubmitField(u'注册')
'''   '''
class loginForm(Form):
    username = StringField(u'邮箱/用户名',validators = [Required(),Length(1,64)])
    password = PasswordField(u'密码',validators = [Required(),Length(1,64)])
    remember_me = BooleanField(u"记住我")
    submit = SubmitField(u'登录')