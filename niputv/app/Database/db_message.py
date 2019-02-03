# -*- coding: utf-8 -*-
from app import db
from flask_login import current_user
import time

#点赞记录
class Like_comment_record(db.Model):

    #查询 userid 和视频id 取出自己是否点赞过 True为点赞 False踩

    # 表的名字
    __tablename__ = 'like_comment_record'

    id = db.Column(db.Integer, primary_key=True) #自增id
    user_id = db.Column(db.Integer) #操作用户id
    comment_id = db.Column(db.Text) #评论id
    operating_record = db.Column(db.Boolean) #点赞记录 True为点赞 False踩

    # 定义对象
    def __init__(self, id = None, comment_id = None, operating_record = None):
        self.user_id = current_user.id
        self.comment_id = comment_id
        self.operating_record = operating_record
        self.update()  # 提交数据

    # 提交数据函数
    def update(self):
        db.session.add(self)
        db.session.commit()

class Comment(db.Model):

    # 表的名字
    __tablename__ = 'comment'

    id = db.Column(db.Integer, primary_key=True) #自增id
    content_type = db.Column(db.Text) #评论类型
    page_id = db.Column(db.Text) #视频id
    user_id = db.Column(db.Integer) #用户id
    content = db.Column(db.Text) #评论内容
    date = db.Column(db.Text) #发布时间日期
    like_pcs = db.Column(db.Integer) #点赞次数
    dislike_pcs = db.Column(db.Integer) #被踩次数
    secondary_comment = db.Column(db.Integer) #是否存在二级评论
    floor = db.Column(db.Integer) #楼层数

    # 定义对象
    def __init__(self, page_id=None, id=None, content=None, date=None, like_pcs=None, dislike_pcs=None, secondary_comment=None, floor=None, content_type=None):
        self.content_type = content_type
        self.page_id = page_id
        self.user_id = current_user.id
        self.content = content
        self.date = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        self.floor = floor
        self.like_pcs = 0
        self.dislike_pcs = 0
        self.secondary_comment = 0
        self.update()  # 提交数据

    # 提交数据函数
    def update(self):
        db.session.add(self)
        db.session.commit()


class Sub_comment(db.Model):

    # 表的名字
    __tablename__ = 'sub_comment'

    id = db.Column(db.Integer, primary_key=True) #自增id
    comment_id = db.Column(db.Integer) #父级评论id
    user_id = db.Column(db.Integer) #用户id
    content = db.Column(db.Text) #评论内容
    date = db.Column(db.Text) #发布时间日期
    like_pcs = db.Column(db.Integer) #点赞次数
    dislike_pcs = db.Column(db.Integer) #被踩次数

    # 定义对象
    def __init__(self, comment_id=None, id=None, content=None, date=None, like_pcs=0, dislike_pcs=0):
        self.comment_id = comment_id
        self.user_id = current_user.id
        self.content = content
        self.data = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        self.update()  # 提交数据

    # 提交数据函数
    def update(self):
        db.session.add(self)
        db.session.commit()

#db.create_all()