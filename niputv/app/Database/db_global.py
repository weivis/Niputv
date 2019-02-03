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

    # 定义对象
    def __init__(self, maincategory_id=None, name=None, subcategory_url=None, description=None):
        self.maincategory_id = maincategory_id
        self.name = name
        self.subcategory_url = subcategory_url
        self.description = description
        self.update()  # 提交数据

    # 提交数据函数
    def update(self):
        db.session.add(self)
        db.session.commit()


#region
class Region(db.Model):

    # 表的名字
    __tablename__ = 'region'

    id = db.Column(db.Integer, primary_key=True) #自增id
    partition_id = db.Column(db.Integer) #主分区id
    name_cn = db.Column(db.Text) #中文分区名
    name_en = db.Column(db.Text) #英文分区名
    ico = db.Column(db.Text) #分区图标
    cover = db.Column(db.Text) #分区封面

    # 定义对象
    def __init__(self, partition_id=None, name_cn='None', name_en='None', ico='None', cover='None'):
        self.partition_id = partition_id
        self.name_cn = name_cn
        self.name_en = name_en
        self.ico = ico
        self.cover = cover
        self.update()  # 提交数据

    # 提交数据函数
    def update(self):
        db.session.add(self)
        db.session.commit()