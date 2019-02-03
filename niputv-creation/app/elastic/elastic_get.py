from flask_login import current_user
from app.elastic.elastic_config import *
import time    

'''
    must：所有分句都必须匹配，与 AND 相同。
    must_not：所有分句都必须不匹配，与 NOT 相同。
    should：至少有一个分句匹配，与 OR 相同。
'''

def get_getcreation_video(video_type, search, page):

    getfrom = int(page) * 10

    if search == None:
        if video_type == 'all':
            body = {
                "from" : getfrom, "size" : 10,
                "query": {
                    "bool": {
                    "must": [
                        { "match": { "authorid": current_user.id }},
                    ]
                    }
                },
                "sort": {
                    "timestamp": {  # 根据age字段升序排序
                        "order": "desc"  # asc升序，desc降序
                    }
                }
            }

        elif video_type == 'review':
            body = {
                "from" : getfrom, "size" : 10,
                "query": {
                    "bool": {
                    "must": [
                        { "match": { "authorid": current_user.id }},
                        { "match": { "status": 1 }}
                    ]
                    }
                }
            }

        elif video_type == 'return':
            body = {
                "from" : getfrom, "size" : 10,
                "query": {
                    "bool": {
                    "must": [
                        { "match": { "authorid": current_user.id }},
                        { "match": { "status": 2 }}
                    ]
                    }
                }
            }
    else:
        body = {
            "from" : getfrom, "size" : 10,
            "query": {
                "bool": {
                "should": [
                    { "match": { "authorid": current_user.id }},
                    { "match": { "video_name": search }}
                ]
            }
        }
    }

    cache = es.search(index='video', doc_type='video', body=body)

    cache_hits = cache['hits']['hits']

    out = [{
        'partition': i['_source']['partition'],
        'category': i['_source']['category'],
        'video_status' : i['_source']['status'],
        'video_id': i['_id'],
        'video_name': i['_source']['video_name'],
        'video_cover': i['_source']['video_cover'],
        'video_introduction': i['_source']['video_introduction'],
        'video_duration': i['_source']['video_duration'],
        'release_date': i['_source']['release_date'],
        'release_time': i['_source']['release_time'],
        'comment_statistics': i['_source']['comment_statistics'],
        'play_statistics': i['_source']['play_statistics'],
        'like_frequency': i['_source']['like_frequency'],
        'dislike_frequency': i['_source']['dislike_frequency'],
    }for i in cache_hits]
    return out