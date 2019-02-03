from app.elastic.elasticconfig import *
import time

def change_video_reviewtype(id,ctype):
    es.update(index='video', doc_type='video', id=id, body={
        "doc": {
            'status': ctype
        }
    })

def create_newbangumi(name,year,month,status,uploads_week,uploads_time,cv,introduction, cover):
    cachedata = es.index(index="bangumi", doc_type='bangumi', body={
        'name': name,
        'year': year,
        'month': month,
        'shelf': 0, #1=下架 0=正常
        'status': status, #0完结 1连载
        'cover': cover,
        'uploads_week': uploads_week, #0=完结
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

def uploads_bangumi_shelf(id,newtype):
    es.update(index='bangumi', doc_type='bangumi', id=id, body={'doc': { 'shelf': newtype }})

def uploads_bangumi_status(id,newtype):
    es.update(index='bangumi', doc_type='bangumi', id=id, body={'doc': { 'status': newtype }})

def es_del_bangumi(id):
    try:
        es.delete(index='bangumi', doc_type='bangumi', id=id)
        return 'ok'
    except:
        return 'no video id'

def change_bangumi_videopcs(id,ctype):
    data = es.get(index='bangumi', doc_type='bangumi', id=id)
    if ctype == 'up':
        body = {
            "doc": {
                'video_statistics': data['_source']['video_statistics'] + 1
            }
        }
    elif ctype == 'dow':
        body = {
            "doc": {
                'video_statistics': data['_source']['video_statistics'] - 1
            }
        }
    else:
        pass
    es.update(index='bangumi', doc_type='bangumi', id=id, body=body)
