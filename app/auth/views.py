#-*-coding:utf-8-*-
from flask import render_template,flash,redirect,url_for,request
from . import auth
from . import forms
from ..models import User
from .. import db
from flask_login import login_required,login_user,logout_user,current_user
from ..email import send_email

'''before_app_request 修饰器过滤未确认账号'''
@auth.before_app_request
def before_request():
        if current_user.is_authenticated:
            current_user.ping()
            if not current_user.confirmed and request.endpoint[:5] != 'auth.' and request.endpoint != 'static':

                return redirect(url_for('auth.unconfirmed'))

@auth.route('/register',methods = ["GET","POST"])
def register():
    form = forms.registerForm()
    if form.validate_on_submit():
        user = User(email=form.email.data,username=form.username.data,password=form.password.data)
        db.session.add(user)
        db.session.commit()
        token = user.generate_confirm()
        send_email('Confirm Your Account',[user.email],'email/confirm', user=user, token=token)
        return redirect(url_for('main.index'))
    return render_template('auth/register.html',form=form)

@auth.route('/login',methods = ["GET","POST"])
def login():
    form = forms.loginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.username.data).first()
        if user is None:
            user = User.query.filter_by(username=form.username.data).first()
        #
        if user is not None and user.verify_password(form.password.data):
            login_user(user,form.remember_me.data)
            return redirect(url_for('main.index'))

    return render_template('auth/login.html',form=form)


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash('you have been logged out')
    return redirect(url_for('auth.login'))
'''账号确认路由'''
@auth.route('/confirm/<token>')
@login_required
def confirm(token):
    if current_user.confirmed:
        return redirect(url_for('main.index'))
    if current_user.check_confirm(token):
        flash('You have confirmed your account. Thanks!')
    else:
        flash('The confirmation link is invalid or has expired.')
    return redirect(url_for('main.index'))


@auth.route('/unconfirmed')
def unconfirmed():
    if current_user.is_anonymous or current_user.confirmed:
        return redirect(url_for('main.index'))
    return render_template('auth/unconfirmed.html')

@auth.route('/confirm')
@login_required
def resend_confirmation():
    token = current_user.generate_confirm()
    send_email( 'Confirm Your Account',[current_user.email],'email/confirm', user=current_user, token=token)
    flash('A new confirmation email has been sent to you by email.')
    return redirect(url_for('main.index'))