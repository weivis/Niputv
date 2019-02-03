# -*- coding: utf-8 -*-
from app import db
from flask_login import current_user
import time

#收藏视频
class Collection_video(db.Model):

    # 表的名字
    __tablename__ = 'collection_video'

    id = db.Column(db.Integer, primary_key=True) #自增id
    user_id = db.Column(db.Integer) #用户id
    video_id = db.Column(db.Text) #收藏的视频id
    witime = db.Column(db.Text) #收藏日期

    # 定义对象
    def __init__(self, id=None, video_id=None, witime=None):
        self.user_id = current_user.id
        self.video_id = video_id
        self.witime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        self.update()  # 提交数据

    # 提交数据函数
    def update(self):
        db.session.add(self)
        db.session.commit()

        
#关注作者
class Follow_author(db.Model):

    # 表的名字
    __tablename__ = 'follow_author'

    id = db.Column(db.Integer, primary_key=True) #自增id
    user_id = db.Column(db.Integer) #发起订阅用户id
    follow_user = db.Column(db.Integer) #订阅的作者
    followtime = db.Column(db.Text) #订阅日期

    # 定义对象
    def __init__(self, id=None, follow_user=None, followtime=None):
        self.user_id = current_user.id
        self.follow_user = follow_user
        self.followtime = time.strftime("%Y-%m-%d", time.localtime())
        self.update()  # 提交数据

    # 提交数据函数
    def update(self):
        db.session.add(self)
        db.session.commit()

#订阅番剧
class Subscription_bangumi(db.Model):

    # 表的名字
    __tablename__ = 'subscription_bangumi'

    id = db.Column(db.Integer, primary_key=True) #自增id
    sub_user = db.Column(db.Integer) #订阅用户id
    sub_bangumi = db.Column(db.Text) #订阅的番剧
    sub_time = db.Column(db.Text) #订阅日期

    # 定义对象
    def __init__(self, sub_user=None, sub_bangumi=None, sub_time=None):
        self.sub_user = current_user.id
        self.sub_bangumi = sub_bangumi
        self.sub_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        self.update()  # 提交数据

    # 提交数据函数
    def update(self):
        db.session.add(self)
        db.session.commit()

#添加点赞记录
def add_collection_video(videoid):
    data = Collection_video(video_id=videoid)
    db.session.add(data)
    db.session.commit()