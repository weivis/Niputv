# -*- coding: utf-8 -*-
from app import db
from flask_login import current_user
import time

#点赞记录
class Like_video_record(db.Model):

    #查询 userid 和视频id 取出自己是否点赞过 True为点赞 False踩

    # 表的名字
    __tablename__ = 'like_video_record'

    id = db.Column(db.Integer, primary_key=True) #自增id
    user_id = db.Column(db.Integer) #操作用户id
    videoid = db.Column(db.Text) #视频id
    operating_record = db.Column(db.Boolean) #点赞记录 True为点赞 False踩

    # 定义对象
    def __init__(self, user_id = None, videoid = None, operating_record = None):
        self.user_id = current_user.id
        self.videoid = videoid
        self.operating_record = operating_record
        self.update()  # 提交数据

    # 提交数据函数
    def update(self):
        db.session.add(self)
        db.session.commit()


#播放记录
class Play_recording(db.Model):

    # 表的名字
    __tablename__ = 'play_recording'

    id = db.Column(db.Integer, primary_key=True) #自增id
    user_id = db.Column(db.Integer)
    video_id = db.Column(db.Integer)
    time = db.Column(db.Text)

    # 定义对象
    def __init__(self, id=None, video_id=None, time=None):
        self.user_id = current_user.id
        self.video_id = video_id
        self.time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        self.update()  # 提交数据

    # 提交数据函数
    def update(self):
        db.session.add(self)
        db.session.commit()


#添加点赞记录
def add_video_likerecord(videoid,putype):
    print(putype)
    data = Like_video_record(videoid=videoid, user_id=current_user.id, operating_record=putype)
    db.session.add(data)
    db.session.commit()

#查询点赞记录
def get_video_likerecord(videoid, putype):
    data = Like_video_record.query.filter_by(videoid=videoid , user_id=current_user.id, operating_record=putype).first()
    return data

#获取指定视频所有点赞记录
def get_video_likerecord_userall(videoid):
    data = Like_video_record.query.filter_by(videoid=videoid , user_id=current_user.id).all()
    return data

#删除记录
def del_video_likerecord(videoid, putype):
    data = Like_video_record.query.filter_by(videoid=videoid, user_id=current_user.id, operating_record=putype).first()
    db.session.delete(data)
    db.session.commit()