__author__ = 'Ran'
from app import Flask, cache, login_manager
from ..works import works
from app.account import Account
from flask_login import current_user, login_required
from flask import render_template, request, session, redirect

from app.elastic.elastic_get import get_getcreation_video
from app.elastic.elastic_video_operating import es_del_video, es_query_video
from app.elastic.elastic_tag import video_all_tag
from app.cloud import del_video_file
from app.Database.db_user import video_quantity_delete
import json

#首页
@works.route('/')
@login_required
def home():
    return render_template('creation/video.html')

#获取用户视频api
@works.route('/creation-api/getvideo/<video_type>/name/<name>/page/<page>', methods=["POST"])
@login_required
def get_creation_video(video_type, name, page):
    data = []
    if name == 'None':
        if video_type == '0':
            data = get_getcreation_video('all',None,page)

        elif video_type == '1':
            data = get_getcreation_video('review',None,page)

        elif video_type == '2':
            data = get_getcreation_video('return',None,page)
    else:
        data = get_getcreation_video(None,name,page)
    
    return json.dumps(data)

@works.route('/api/del/<videoid>')
@login_required
def del_video(videoid):
    if(videoid):
        data = es_query_video(videoid)
        if data['_source']['authorid'] == current_user.id:
            es_del_video(data['_id'])
            del_video_file(videoid)
            video_quantity_delete()
            video_all_tag(videoid)
            return json.dumps({'code':'ok'})
        else:
            return json.dumps({'code':'error', 'type':'fuck you sb'})
    else:
        return json.dumps({'code':'error', 'type':'fuck you sb'})