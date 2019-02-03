from flask import Flask
from flask_sqlalchemy import SQLAlchemy

#DEBUG = True

# Flask Sqlalchemy Setting

SQLALCHEMY_DATABASE_URI = 'mysql://root:@localhost:3307/niputv?charset=utf8'
SQLALCHEMY_TRACK_MODIFICATIONS = False
# Flask Bcrypt Setting
BCRYPT_LOG_ROUNDS = 1