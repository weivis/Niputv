# -*- coding: utf-8 -*-
from app import db
from flask_login import current_user

class Account(db.Model):
    __tablename__ = 'Account'#用户数据

    id = db.Column(db.Integer, primary_key=True) #用户id
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
    def __init__(self, id=None, introduction=None, works_quantity=0, dislike_statistics=0, like_statistics=0, fan_statistics=0, play_quantity=0, space_introduction=None, topping_video=None, system_new=0, reply_new=0, at_new=0):
        self.id = current_user.id
        self.introduction = introduction
        self.works_quantity = works_quantity
        self.dislike_statistics = dislike_statistics
        self.like_statistics = like_statistics
        self.fan_statistics = fan_statistics
        self.play_quantity = play_quantity
        self.space_introduction = space_introduction
        self.topping_video = topping_video
        self.update()  # 提交数据

    # 提交数据函数
    def update(self):
        db.session.add(self)
        db.session.commit()
        
#更新视频数量 + 1 不存在记录 则写入 = 1
def video_quantity_plus():
    data = Account.query.filter_by(id = current_user.id).first()
    if(data):
        newquantity = data.works_quantity + 1
        db.session.query(Account).filter(Account.id == current_user.id).update({Account.works_quantity:newquantity})
        db.session.commit()
    else:
        data = Account(works_quantity = 1)
        db.session.add(data)
        db.session.commit()

#删除视频 -1 视频小于0时 报错
def video_quantity_delete():
    data = Account.query.filter_by(id = current_user.id).first()
    if(data):
        if(data.works_quantity > 0):
            newquantity = data.works_quantity - 1
            db.session.query(Account).filter(Account.id == current_user.id).update({Account.works_quantity:newquantity})
            db.session.commit()

