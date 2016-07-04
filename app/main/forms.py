#-*-coding:utf-8-*-
from flask_wtf import Form
from wtforms import StringField,TextAreaField,SubmitField,BooleanField,SelectField
from wtforms.validators import Length,Required,Email,Regexp
from wtforms import ValidationError
from ..models import User,Role
from flask_pagedown.fields import PageDownField

class EditProfileForm(Form):
    name = StringField('Real name', validators=[Length(0, 64)])
    location = StringField('Location', validators=[Length(0, 64)])
    about_me = TextAreaField('About me')
    submit = SubmitField('Submit')

class EditProfileAdminForm(Form):
    email = StringField('Email', validators=[Required(), Length(1, 64),Email()])
    username = StringField('Username', validators=[Required(), Length(1, 64), Regexp('^[A-Za-z][A-Za-z0-9_.]*$', 0,
                            u'用户名必须只包含字母，数字或下划线')])
    confirmed = BooleanField('Confirmed')
    role = SelectField('Role', coerce=int)
    name = StringField('Real name', validators=[Length(0, 64)])
    location = StringField('Location', validators=[Length(0, 64)])
    about_me = TextAreaField('About me')
    submit = SubmitField('Submit')
    def __init__(self, user, *args, **kwargs):
        super(EditProfileAdminForm, self).__init__(*args, **kwargs)
        self.role.choices = [(role.id, role.name)for role in Role.query.order_by(Role.name).all()]
        self.user = user
    def validate_email(self, field):
        if field.data != self.user.email and \
        User.query.filter_by(email=field.data).first():
            raise ValidationError('Email already registered.')
    def validate_username(self, field):
        if field.data != self.user.username and \
            User.query.filter_by(username=field.data).first():
            raise ValidationError('Username already in use.')

class PostForm(Form):
    body = PageDownField("What's on your mind?", validators=[Required()])
    submit = SubmitField(u'发布')

class CommentForm(Form):
    body = StringField('', validators=[Required()])
    submit = SubmitField(u'评论')