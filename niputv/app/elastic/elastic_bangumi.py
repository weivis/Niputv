from app.elastic.elastic_config import *
from app.Database.db_global import Category
import time

def create_newbangumi(name,year,month,status,uploads_week,uploads_time,cv,introduction, cover):
    cachedata = es.index(index="bangumi", doc_type='bangumi', body={
        'name': name,
        'year': year,
        'month': month,
        'shelf': 0, #1=下架 0=正常
        'status': status, #0完结 1连载
        'cover': cover,
        'uploads_week': uploads_week,
        'uploads_time': uploads_time,
        'cv': cv,
        'introduction': introduction,
        'video_statistics': 0, #视频数量统计
        'play_statistics': 0, #播放数统计
        'sub_statistics': 0, #追番数统计
        'like_frequency': 0, #喜欢统计
        'dislike_frequency': 0, #不喜欢统计
        'creation_time': time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), #创建日期
    })
    es.indices.refresh(index="bangumi")
    return cachedata['_id']


def query_bangumi_data(id):
    if (id):
        data = es.get(index='bangumi', doc_type='bangumi', id=id)
        if (data):
            return data
        else:
            return ''
    else:
        return 'error:no id'


def query_shelf_bangumi_list():
    body = {
        "size" : 50,
        "query": {
            "bool": {
            "must": [
                { "match": { "shelf": 0 }},#0=正常 1=下架
                #{ "match": { "status": 0 }}
            ]
            }
        }
    }
    data = es.search(index='bangumi', doc_type='bangumi', body=body)
    hits = data['hits']['hits']
    list = [{
        'id':data['_id'],
        'name':data['_source']['name'],
        'cover': data['_source']['cover'],
        'uploads_week': data['_source']['uploads_week'],
        'video_statistics': data['_source']['video_statistics'],
        'shelf': data['_source']['shelf']
    }for data in hits]
    return list

def query_shelf_bangumi_wanjie():
    body = {
        "size" : 30,
        "query": {
            "bool": {
            "must": [
                { "match": { "shelf": 0 }},#0=正常 1=下架
                #{ "match": { "status": 0 }}
            ]
            }
        }
    }
    data = es.search(index='bangumi', doc_type='bangumi', body=body)
    hits = data['hits']['hits']
    list = [{
        'id':data['_id'],
        'name':data['_source']['name'],
        'cover': data['_source']['cover'],
        'uploads_week': data['_source']['uploads_week'],
        'video_statistics': data['_source']['video_statistics'],
        'shelf': data['_source']['shelf']
    }for data in hits]
    return list

def adddel_bangumi_sub_statistics(tp,id):
    if tp == 'add':
        videodata = es.get(index='bangumi', doc_type='bangumi', id=id)
        body={
            "doc": {
                'sub_statistics': videodata['_source']['sub_statistics'] + 1
            }
        }
        es.update(index='bangumi', doc_type='bangumi', id=id, body=body)

    elif tp == 'del':
        videodata = es.get(index='bangumi', doc_type='bangumi', id=id)
        body={
            "doc": {
                'sub_statistics': videodata['_source']['sub_statistics'] - 1
            }
        }
        es.update(index='bangumi', doc_type='bangumi', id=id, body=body)
    else:
        pass