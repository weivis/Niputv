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
        #self.videoid = videoid
        self.filekey = filekey
        self.upload_userid = current_user.id
        self.update()  # 提交数据

    # 提交数据函数
    def update(self):
        db.session.add(self)
        db.session.commit()

# 番剧剧集
class Bangumi_video(db.Model):

    # 表的名字
    __tablename__ = 'bangumi_video'

    id = db.Column(db.Integer, primary_key=True) #自增id
    upload_adminid = db.Column(db.Integer) #上传者
    cover = db.Column(db.Text) #封面
    bangumi_id = db.Column(db.Text) #父级番剧id
    video_name = db.Column(db.Text) #剧集名
    video_sort = db.Column(db.Text) #剧集数
    upload_date = db.Column(db.Text) #上传日期
    filekey = db.Column(db.Text) #视频文件
    clear360 = db.Column(db.Boolean)
    clear480 = db.Column(db.Boolean)
    clear720 = db.Column(db.Boolean)
    clear1080 = db.Column(db.Boolean)

    # 定义对象
    def __init__(self, cover=None, upload_adminid=None, bangumi_id=None, video_name=None, video_sort=None, upload_date=None, filekey=None, clear360=None, clear480=None, clear720=None, clear1080=None):
        self.cover = cover
        self.upload_adminid = current_user.id
        self.bangumi_id = bangumi_id
        self.video_name = video_name
        self.video_sort = video_sort
        self.upload_date = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        self.filekey = filekey
        self.update()  # 提交数据

    # 提交数据函数
    def update(self):
        db.session.add(self)
        db.session.commit()