__author__ = 'Ran'
from app import Flask, cache
from ..index import index
from flask import render_template, request, session, redirect

#首页
@index.route('/')
def home():
    return render_template('index/index.html')