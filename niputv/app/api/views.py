# -*- coding: utf-8 -*-
__author__ = 'Ran'
from ..api import api
from app import Flask, db, cache
from flask import render_template, request, redirect, make_response
from app.Database.db_global import Partition, Category
from app.Database.db_features import Collection_video, add_collection_video, Subscription_bangumi
from app.elastic.elastic_global import es_query_video
from app.elastic.elastic_query import elastic_query_indexmodule_data
from app.elastic.elastic_tag import get_videoalltag
from app.Database.db_operatingrecord import get_video_likerecord, add_video_likerecord, del_video_likerecord, get_video_likerecord_userall
from app.elastic.elastic_video_operating import video_likeadd
from app.follow.follow_user import follow_orm, follow_gettype
from app.msg.comment import write_comment, get_commentlist, likecomment_pus
from flask_login import current_user
from app.account import Account
from app.middleware.get_cacheuser import get_middleware_account
from app.recommend_ai.business import get_recommend_videolist
from app.tag.tag_business import write_Atag
import json
from app.follow.follow_bangumi import delbangumisub, addbangumisub

from app.middleware.login_auth import auth_is_login #@auth_is_login
from functools import wraps

def allow_cross_domain(fun):
    @wraps(fun)
    def wrapper_fun(*args, **kwargs):
        rst = make_response(fun(*args, **kwargs))
        rst.headers['Access-Control-Allow-Origin'] = '*'
        rst.headers['Access-Control-Allow-Methods'] = 'PUT,GET,POST,DELETE'
        allow_headers = "Referer,Accept,Origin,User-Agent"
        rst.headers['Access-Control-Allow-Headers'] = allow_headers
        return rst
    return wrapper_fun

#首页
@api.route('/nav')
@allow_cross_domain
#@cache.cached(timeout=3600, key_prefix='global_nav')
def nav_api():
    data = Partition.query.filter_by().all()
    list = [{
        'ico':i.ico,
        'title': i.name,
        'url': i.maincategory_url,
        'sort': i.sort,
    }for i in data]
    return json.dumps(sorted(list, key=lambda x:x['sort'], reverse=True))

#首页-模块接口
@api.route('/index-content/module/<gettype>/<name>')
def getapi_indexmodule(gettype, name):

    '''
    category = 子分区
    partition = 主分区
    '''

    if gettype == 'partition':
        data = elastic_query_indexmodule_data("partition",name)
        return json.dumps(data)
    elif gettype == 'category':
        data = elastic_query_indexmodule_data("category",name)
        return json.dumps(data)
    elif gettype == 'all':
        data = elastic_query_indexmodule_data("all",name)
        return json.dumps(data)
    else:
        pass
        data = []
        return json.dumps(data)

#点赞记录
@api.route('/video/videolike-type', methods=["POST"])
@auth_is_login
def videolike_typeget():
    if current_user.is_authenticated :
        video = request.args.get('video')
        data = get_video_likerecord_userall(videoid=video)
        videodata = es_query_video(video)
        list = [{
            'code':i.operating_record
        }for i in data]
        likenaber = {
            "like_frequency": videodata['_source']['like_frequency'],
            "dislike_frequency": videodata['_source']['dislike_frequency']
        }
        p = {
            "type":list,
            "naber":likenaber
        }
        return json.dumps(p)
    else:
        return json.dumps({"like_frequency": 0, "dislike_frequency": 0})

#点赞
@api.route('/video/videolike', methods=["POST"])
@auth_is_login
def videolike():
    if(current_user):
        video = request.args.get('video')
        putype = request.args.get('type')

        if putype == 'True':
            putype = True
        elif putype == 'False':
            putype = False
        else:
            return 'fuck you sb'

        #查询视频点赞记录和点赞类型
        data = get_video_likerecord(videoid=video, putype=putype)

        #如果存在则删除
        if (data):
            video_likeadd(videoid=video, settype=putype, settype2='del')
            del_video_likerecord(videoid=video, putype=putype)
            return json.dumps({'code':'ok'})

        else:
            #不存在则写入
            video_likeadd(videoid=video, settype=putype, settype2='add')
            add_video_likerecord(videoid=video, putype=putype)
            return json.dumps({'code':'ok'})
    else:
        return json.dumps({'code':'error'})

#收藏
@api.route('/video/collection', methods=["POST"])
@auth_is_login
def videocollection():
    if current_user.is_authenticated:
        video = request.args.get('video')
        add_collection_video(video)
        return json.dumps({'code':'ok'})
    else:
        return json.dumps({'code':'error'})

#收藏
@api.route('/video/collection_type', methods=["POST"])
@auth_is_login
def videocollection_type():
    if current_user.is_authenticated:
        video = request.args.get('video')
        data = Collection_video.query.filter_by(video_id=video, user_id=current_user.id).first()
        if (data):
            return json.dumps({'code':'1'})
        else:
            return json.dumps({'code':'0'})
    else:
        return json.dumps({'code':'error'})

#获取视频up主
@api.route('/video/up', methods=["POST"])
def video_upapi():
    key = request.args.get('key')
    data = get_middleware_account(id=int(key))
    com_account = Account.query.filter_by(id=int(key)).first()
    list = {
        'name': data.username,
        'head': data.head,
        'introduction': com_account.introduction,
        'fan_statistics': com_account.fan_statistics,
    }
    return json.dumps(list)

#视频分区类型
@api.route('/video/class/<cla>/tab/<tab>', methods=["POST"])
@cache.cached(timeout=3600, key_prefix='video_type_%s')
def video_classget(cla, tab):
    data = Partition.query.filter_by(id=cla).first()
    tabdata = Category.query.filter_by(id=tab).first()
    list = {
        'partition':data.name,
        'category':tabdata.name,
    }
    return json.dumps(list)

#订阅作者
@api.route('/video/follow_auth/<authid>', methods=["POST"])
@auth_is_login
def follow_auth(authid):
    data = follow_orm(authid)
    return json.dumps({'code':data})

#订阅状态
@api.route('/video/follow_type/<authid>', methods=["POST"])
@auth_is_login
def follow_type(authid):
    if current_user.is_authenticated:
        data = follow_gettype(authid)
        return json.dumps({'code':data})
    else:
        return json.dumps({'code':False})

#发送评论
@api.route('/global/comment/<id>/<contenttype>', methods=["POST"])
@auth_is_login
def video_comment(id, contenttype):
    content = request.form.get('content')
    if contenttype == 'video' or 'bangumi':
        data = write_comment(content=content, video_id=id, contenttype=contenttype)
    else:
        return json.dumps({'code':'you is sb'})
    list={
        'content':content,
        'head':current_user.head,
        'id': data.id,
        'user': current_user.username,
        'time': data.date,
        'like_pcs': data.like_pcs,
        'dislike_pcs': data.dislike_pcs,
        'secondary_comment': data.secondary_comment,
    }
    return json.dumps(list)

#评论获取列表
@api.route('/global/comment-list/<id>/<int:page>/<gettype>/<contenttype>', methods=["POST"])
def video_comment_list(id, page, gettype,contenttype):
    if gettype == 'false': #like_pcs #time
        gettype == False
    data = get_commentlist(id ,page, gettype, contenttype)
    return json.dumps(data)

#评论点赞
@api.route('/global/comment-pus/<id>/type/<clss>', methods=["POST"])
@auth_is_login
def video_comment_pus(id,clss):
    if clss == 'like':
        data=likecomment_pus(commentid = id, pustype='like')
    elif clss == 'nolike':
        data=likecomment_pus(commentid = id, pustype='nolike')
    return json.dumps(data)

#相关视频列表
@api.route('/video/recommend/<up>/<videoname>', methods=["POST"])
def video_recommend(up, videoname):
    data = get_recommend_videolist(up, videoname)
    return json.dumps(data)

#tag获取
@api.route('/video/tag/get/<vid>', methods=["POST"])
def video_gettag(vid):
    data = get_videoalltag(vid)
    return json.dumps(data)

#tag添加
@api.route('/video/tag/add-tag', methods=["POST"])
@auth_is_login
def video_addtag():
    if(current_user):
        data = request.json
        print(data)
        videoid = data['videoid']
        tag = data['tag']
        try:
            videodata = es_query_video(videoid)
            if videodata['_source']['authid'] == current_user.user_id:
                write_Atag(tag=tag,vid=videoid)
                return json.dumps({'code':1})
            else:
                return json.dumps({'code':2})
        except:
            return json.dumps({'code':'error'})

#订阅番剧和取消订阅
@api.route('/bangumi/follow-bangumi', methods=["POST"])
@auth_is_login
def follow_bangumi():
    if(current_user):
        jsondata = request.json
        sub = Subscription_bangumi.query.filter_by(sub_user=current_user.id, sub_bangumi=jsondata['bangumi']).first()
        if (sub):
            #存在事件则删除
            delbangumisub(sub)
            return json.dumps({'code':'delsub'})
        else:
            #不存在则订阅事件
            addbangumisub(jsondata['bangumi'])
            return json.dumps({'code':'addsub'})

#订阅番剧和取消订阅
@api.route('/bangumi/follow-bangumi-type', methods=["POST"])
@auth_is_login
def follow_bangumi_get():
    if(current_user):
        jsondata = request.json
        sub = Subscription_bangumi.query.filter_by(sub_user=current_user.id, sub_bangumi=jsondata['bangumi']).first()
        if (sub):
            return json.dumps({'code':True})
        else:
            return json.dumps({'code':False})