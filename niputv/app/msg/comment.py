# -*- coding: utf-8 -*-
from app import Flask, db, cache
from app.account import Account
from app.Database.db_message import Comment, Like_comment_record
from flask_login import current_user
from app.middleware.get_cacheuser import get_middleware_account
from app.elastic.elastic_video_operating import upadd_commentpcs
from app.Database.db_video import Bangumi_video

def write_comment(content, video_id, contenttype):
    data = Comment(content=content, page_id=video_id, content_type=contenttype)
    db.session.add(data)
    db.session.commit()
    if contenttype == 'video':
        upadd_commentpcs(video_id)
    elif contenttype == 'bangumi':
        data = Bangumi_video.query.filter_by(id = video_id).first()
    else:
        print('出错')
    return data

def get_commentlist(video_id, page, gettype, contenttype):
    if page == 0:
        naber = 1
    else:
        naber = page

    if gettype == 'like_pcs':
        data = Comment.query.filter_by(page_id = video_id, content_type=contenttype).order_by("like_pcs").limit(int(naber*10)).offset(page)
    elif gettype == 'time':
        data = Comment.query.filter_by(page_id = video_id, content_type=contenttype).order_by("date").limit(int(naber*10)).offset(page)
    else:
        data = Comment.query.filter_by(page_id = video_id, content_type=contenttype).order_by("id").limit(int(naber*10)).offset(page)

    datalist = [{
        'id': i.id,
        'content': i.content,
        'head': (get_middleware_account(int(i.user_id))).head,
        'user': (get_middleware_account(int(i.user_id))).username,
        'time': i.date,
        'like_pcs': i.like_pcs,
        'dislike_pcs': i.dislike_pcs,
        'secondary_comment': i.secondary_comment,
        'like_type': likedlik_type(i.id,'like'),
        'dislike_type': likedlik_type(i.id,'dislike'),
    }for i in data]
    return datalist

def likecomment_pus(commentid, pustype):
    #判断传入类型是喜欢还是踩
    if pustype == 'like':

        #操作记录表 评论id=评论id 发布者id=用户id 操作类型=true（1）
        data = Like_comment_record.query.filter_by(comment_id = commentid, user_id = current_user.id, operating_record = 1).first()

        commentiddata = Comment.query.filter_by(id=commentid).first()

        #判断是否已经点赞过(是否存在此记录)(如果有则存在 表示已经点赞过)
        if(data):
            #点赞过要删除点赞记录 和 点赞统计-1
            newpcs = commentiddata.like_pcs - 1
            db.session.query(Comment).filter(Comment.id == commentid).update({Comment.like_pcs:newpcs}) #更新主评论点赞统计数 -1

            #存在则删除记录
            db.session.delete(data)
            db.session.commit()

        else:
            #不存在则添加
            newpcs = commentiddata.like_pcs + 1
            db.session.query(Comment).filter(Comment.id == commentid).update({Comment.like_pcs:newpcs}) #更新主评论点赞统计数 +1
            #添加记录
            newdata = Like_comment_record(comment_id=commentid, operating_record=True)
            db.session.add(newdata)
            db.session.commit()

    elif pustype == 'nolike':
        data = Like_comment_record.query.filter_by(comment_id = commentid, user_id = current_user.id, operating_record = 0).first()

        commentiddata = Comment.query.filter_by(id=commentid).first()

        #判断是否已经点赞过(是否存在此记录)(如果有则存在 表示已经点赞过)
        if(data):
            #点赞过要删除点赞记录 和 点赞统计-1
            newpcs = commentiddata.dislike_pcs - 1
            db.session.query(Comment).filter(Comment.id == commentid).update({Comment.dislike_pcs:newpcs}) #更新主评论踩统计数 +1

            #存在则删除记录
            db.session.delete(data)
            db.session.commit()

        else:
            #不存在则添加
            newpcs = commentiddata.dislike_pcs + 1
            db.session.query(Comment).filter(Comment.id == commentid).update({Comment.dislike_pcs:newpcs}) #更新主评论踩统计数 +1
            #添加记录
            newdata = Like_comment_record(comment_id=commentid, operating_record=False)
            db.session.add(newdata)
            db.session.commit()


def likedlik_type(id,getype):
    if current_user.is_authenticated:
        if getype == 'like':
            if Like_comment_record.query.filter_by(comment_id = id, user_id = current_user.id, operating_record = 1).first():
                return True
            else:
                return False
        if getype == 'dislike':
            if Like_comment_record.query.filter_by(comment_id = id, user_id = current_user.id, operating_record = 0).first():
                return True
            else:
                return False
    else:
        return False