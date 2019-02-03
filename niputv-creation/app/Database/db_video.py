# -*- coding: utf-8 -*-
from app import db
from flask_login import current_user

class Videofile(db.Model):

    # 表的名字
    __tablename__ = 'videofile'

    id = db.Column(db.Integer, primary_key=True) #自增id
    videoid = db.Column(db.Text) #视频 不存在视频id视为空文件
    filekey = db.Column(db.Text) #视频
    upload_userid = db.Column(db.Integer) #上传者
    clear360 = db.Column(db.Boolean)
    clear480 = db.Column(db.Boolean)
    clear720 = db.Column(db.Boolean)
    clear1080 = db.Column(db.Boolean)
    clear2k = db.Column(db.Boolean)
    clear4k = db.Column(db.Boolean)

    # 定义对象
    def __init__(self, videoid=None, filekey=None, upload_userid=None, clear360=None, clear480=None, clear720=None, clear1080=None, clear2k=None, clear4k=None):
        self.videoid = videoid #写入视频id
        self.filekey = filekey #视频文件

        self.upload_userid = current_user.id #上传者

        self.clear360 = clear360
        self.clear480 = clear480
        self.clear720 = clear720
        self.clear1080 = clear1080
        self.clear2k = clear2k
        self.clear4k = clear4k
        self.update()  # 提交数据

    # 提交数据函数
    def update(self):
        db.session.add(self)
        db.session.commit()