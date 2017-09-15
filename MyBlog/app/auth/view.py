# -*- coding: utf-8 -*-
from flask import render_template,redirect,url_for,request,flash
from . import auth

from forms import LoginForm, RegistrationForm
from .. import db
from models import User, Role
from flask_login import login_user, logout_user


@auth.route('/')
def index():
    return render_template('index.html')


@auth.route('/login', methods=['GET', 'POST'])
def login():
    form0 = LoginForm()
    if request.method == 'POST':
        if form0.validate_on_submit():
            user = User.query.filter_by(name = form0.username.data, password = form0.password.data).first()
            if user is not None:
                login_user(user)
                return redirect(url_for('main.index'))
        else:
            return '<h1>登录失败！</h1>'
    return render_template('login.html',
                           title=u'登录',
                           form0=form0)


@auth.route('/lougout', methods=['GET', 'POST'])
def logout():
    logout_user()
    return redirect(url_for('auth.login'))


@auth.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            user = User(email=form.email.data,
                        name=form.username.data,
                        password=form.password.data)
            db.session.add(user)
            db.session.commit()
            return redirect(url_for('auth.login'))
        else:
            return render_template('register.html',
                           title=u'注册',
                           form=form)
    return render_template('register.html',
                           title=u'注册',
                           form=form)
