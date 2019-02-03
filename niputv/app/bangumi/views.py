__author__ = 'Ran'
from app import Flask, cache
from ..bangumi import bangumi
from flask import render_template, request, session, redirect
from app.elastic.elastic_bangumi import query_shelf_bangumi_list, query_bangumi_data, query_shelf_bangumi_wanjie
from app.Database.db_video import Bangumi_video
from app.elastic.elastic_global import es_query_bangumi
from app.elastic.elastic_tag import get_bangumialltag
import json

#首页番剧模块api
@bangumi.route('/api/index-module')
def index_bangumijson():
    return json.dumps(query_shelf_bangumi_list())

#番剧首页
@bangumi.route('/')
@cache.cached(timeout=10, key_prefix='bangumi_%s')
def bangumi_home():
    return render_template('index/bangumi-index.html')

#番剧首页已完结接口
@bangumi.route('/api/bangumi-remen')
def bangumi_index_donga_wanjie():
    return json.dumps(query_shelf_bangumi_wanjie())

#番剧-番剧信息剧集
@bangumi.route('/donga/<id>')
@cache.cached(timeout=10, key_prefix='bangumi-watch_%s')
def bangumi_donga(id):
    return render_template('index/bangumi-info.html')

#番剧-番剧信息剧集-番剧资料api
@bangumi.route('/api/bangumi-info/<id>')
def index_bangumi_info(id):
    data = query_bangumi_data(id)
    a = {
        'id': data['_id'],
        'cover': data['_source']['cover'],
        'cv': data['_source']['cv'],
        'name': data['_source']['name'],
        'introduction': data['_source']['introduction'],
        'status': data['_source']['status'],
        'year': data['_source']['year'],
        'month': data['_source']['month'],
        'uploads_week': data['_source']['uploads_week'],
        'uploads_time': data['_source']['uploads_time'],
        'play_statistics': data['_source']['play_statistics'],
        'sub_statistics': data['_source']['sub_statistics'],
        'like_frequency': data['_source']['like_frequency'],
        'dislike_frequency': data['_source']['dislike_frequency'],
        'video_statistics': data['_source']['video_statistics'],
        'tag': get_bangumialltag(id)
    }
    return json.dumps(a)

@bangumi.route('/api/bangumi-videolist/<id>')
def index_bangumi_videolist(id):
    data = Bangumi_video.query.filter_by(bangumi_id=id).all()
    jsondata = [{
        'id': i.id,
        'video_name': i.video_name,
        'video_sort': i.video_sort,
        'cover': i.cover,
        'time': i.upload_date
    }for i in data]
    return json.dumps(sorted(jsondata, key=lambda x:int(x['video_sort']), reverse=True))

#番剧播放
@bangumi.route('/watch/<id>')
def bangumi_watch_page(id):
    videodata = Bangumi_video.query.filter_by(id=id).first()
    if(videodata):
        video_file = {
            "key":videodata.filekey,
            "360":videodata.clear360,
            "480":videodata.clear480,
            "720":videodata.clear720,
            "1080":videodata.clear1080
        }
        video_info = {
            "id":id,
            "bangumi_id":videodata.bangumi_id,
            "sort":videodata.video_sort,
            "comment_statistics":0}
    else:
        video_info = False
        video_file = False
    return render_template('watch/bangumi-watch.html', key = json.dumps(video_file), bangumi_id = json.dumps(video_info), pagid=id)