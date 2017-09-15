# -*- coding: utf-8 -*-

from flask_wtf import Form
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length, EqualTo, Regexp


class LoginForm(Form):
    username = StringField(label=u'用户名：')
    password = PasswordField(label=u'密码：', validators=[DataRequired()])
    submit = SubmitField(label=u'提交')

class RegistrationForm(Form):
    email = StringField(u'邮箱：', validators=[DataRequired(),
                                                  Length(1, 64),
                                                  Email()])
    username = StringField(u'用户名：', validators=[DataRequired(),
                                                      Length(1,64), Regexp('^[a-z]{6,10}$')])#此处省略了正则表达式Regexp('^[A-Za-z][A-Za-z0-9_.]*$')
    password = PasswordField(u'密码', validators=[DataRequired(),
                                                      EqualTo('password2', message=u'密码必须一致')])
    password2 = PasswordField(u'密码', validators=[DataRequired()])
    submit=SubmitField(u'马上注册')