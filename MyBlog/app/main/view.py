from flask import render_template,redirect,url_for,request,flash

from . import main

@main.route('/index')
def index():
    return render_template('index.html')
