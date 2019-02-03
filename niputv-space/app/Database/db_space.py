# -*- coding: utf-8 -*-
from app import db
from flask_login import current_user

# 用户数据表
class Space_userpg(db.Model):

    # 表的名字
    __tablename__ = 'space_userpg'
    __bind_key__ = 'niputv-space'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer)
    pgname = db.Column(db.Text)
    pginfo = db.Column(db.Text)
    pg_videopcs_statistics = db.Column(db.Integer)

    # 定义对象
    def __init__(self, user_id=None, pgname=None, pginfo=None, pg_videopcs_statistics=0):
        self.user_id = current_user.id
        self.pgname = pgname
        self.update()  # 提交数据

    # 提交数据函数
    def update(self):
        db.session.add(self)
        db.session.commit()

# 用户数据表
class Space_pg_video(db.Model):

    # 表的名字
    __tablename__ = 'space_pg_video'
    __bind_key__ = 'niputv-space'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer)
    pgid = db.Column(db.Integer)
    videoid = db.Column(db.Text)
    time = db.Column(db.Text)

    # 定义对象
    def __init__(self, pgid, videoid, time):
        self.user_id = current_user.id
        self.videoid = videoid
        self.pgid = pgid
        self.time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        self.update()  # 提交数据

    # 提交数据函数
    def update(self):
        db.session.add(self)
        db.session.commit()

db.create_all()