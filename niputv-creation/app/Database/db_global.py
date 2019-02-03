# -*- coding: utf-8 -*-
from app import db
from flask_login import current_user

class Partition(db.Model):

    # 表的名字
    __tablename__ = 'partition'

    id = db.Column(db.Integer, primary_key=True) #自增id
    name = db.Column(db.Text) #分区名
    maincategory_url = db.Column(db.Text) #分区路径
    sort = db.Column(db.Integer)
    ico = db.Column(db.Text)


    # 定义对象
    def __init__(self, name=None, maincategory_url=None, ico=None):
        self.ico = ico
        self.name = name
        self.maincategory_url = maincategory_url
        self.update()  # 提交数据

    # 提交数据函数
    def update(self):
        db.session.add(self)
        db.session.commit()

class Category(db.Model):

    # 表的名字
    __tablename__ = 'category'

    id = db.Column(db.Integer, primary_key=True) #自增id
    partition_id = db.Column(db.Integer) #主分区id
    name = db.Column(db.Text) #分区名
    subcategory_url = db.Column(db.Text) #分区路径
    description = db.Column(db.Text) #分区介绍或描述
    sort = db.Column(db.Integer)
    uploadvideo = db.Column(db.Integer)
    allow = db.Column(db.Integer)

    # 定义对象
    def __init__(self, maincategory_id=None, name=None, subcategory_url=None, description=None, allow=0):
        self.maincategory_id = maincategory_id
        self.name = name
        self.subcategory_url = subcategory_url
        self.description = description
        self.update()  # 提交数据

    # 提交数据函数
    def update(self):
        db.session.add(self)
        db.session.commit()

def upload_category_upcount(id):
    data = Category.query.filter_by(id = id).first()
    if(data):
        if data.uploadvideo == 0:
            newquantity = 1
        else:
            newquantity = data.uploadvideo + 1

        db.session.query(Category).filter(Category.id == id).update({Category.uploadvideo:newquantity})
        db.session.commit()