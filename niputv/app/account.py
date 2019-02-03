# -*- coding: utf-8 -*-
from app import db, login_manager
from flask_login import UserMixin

# -----------------------------------------------------------

# 账户表
class Account(db.Model, UserMixin):

    # 表的名字
    __tablename__ = 'account'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True) #用户名不能重复
    password = db.Column(db.String(100))
    head = db.Column(db.Text)
    user_email = db.Column(db.String(150), unique=True) #用户邮箱不能重复
    phone = db.Column(db.String(100), unique=True) #用户手机不能重复
    introduction = db.Column(db.Text) #个人介绍
    works_quantity = db.Column(db.Integer) #上传作品数量
    play_quantity = db.Column(db.Integer) #播放量统计
    fan_statistics = db.Column(db.Integer) #粉丝数统计
    like_statistics = db.Column(db.Integer) #被点赞次数统计
    dislike_statistics = db.Column(db.Integer) #被踩次数统计
    space_introduction = db.Column(db.Text) #空间介绍
    topping_video = db.Column(db.Integer) #置顶视频
    at_new = db.Column(db.Integer) #@消息
    reply_new = db.Column(db.Integer) #回复消息
    system_new = db.Column(db.Integer) #系统消息
    
    # 定义对象
    def __init__(self, head=None, username=None, user_email=None, phone=None, introduction=None, space_introduction=None, topping_video=None,
    works_quantity=0, dislike_statistics=0, like_statistics=0, fan_statistics=0, play_quantity=0):
        self.username = username
        self.usere_mail = user_email
        self.phone = phone
        self.introduction = introduction
        self.works_quantity = works_quantity
        self.dislike_statistics = dislike_statistics
        self.like_statistics = like_statistics
        self.fan_statistics = fan_statistics
        self.play_quantity = play_quantity
        self.space_introduction = space_introduction
        self.topping_video = topping_video
        self.update()  # 提交数据

    #密码检验
    def is_correct_password(self, plaintext):
        if check_password_hash(self.password, plaintext):
            return True

    # 提交数据函数
    def update(self):
        db.session.add(self)
        db.session.commit()

# -----------------------------------------------------------