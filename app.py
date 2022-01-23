# -*- coding: utf-8 -*-
from flask import Flask,redirect,render_template,session,request,Response
import os,sys,random,datetime as niciji

app = Flask(__name__)
app.debug=False

@app.route('/')
def root():
    return 'hello, world<br>こんにちは'

@app.route('/info')
def info():
    tmplData="dictにhtmlへ変数"
    return render_template('info.html',tmpl=tmplData)

@app.route('/index')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    # app.run(debug=True)
    app.run()
