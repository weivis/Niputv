from app.elastic.elastic_config import *

def elastic_query_indexmodule_data(gettype, id):
    if gettype == 'all':
        body = {
            "size" : 12,
            "query": {
                "bool": {
                "must": [
                    { "match": { "status": 0 }}
                ]
                }
            },
            "sort": {
                "play_statistics": {  # 根据age字段升序排序
                    "order": "asc"  # asc升序，desc降序
                },
            }
        }

    elif gettype == 'partition':
        body = {
            "size" : 6,
            "query": {
                "bool": {
                "must": [
                    { "match": { "partition": id }},
                    { "match": { "status": 0 }}
                ]
                }
            },
            "sort": {
                "play_statistics": {  # 根据age字段升序排序
                        "order": "desc"  # asc升序，desc降序
                },
                "like_frequency": {  # 根据age字段升序排序
                    "order": "desc"  # asc升序，desc降序
                }
            }
        }

    elif gettype == 'category':
        body = {
            "size" : 6,
            "query": {
                "bool": {
                "must": [
                    { "match": { "category": id }},
                    { "match": { "status": 0 }}
                ]
                }
            },
            "sort": {
                "play_statistics": {  # 根据age字段升序排序
                    "order": "desc"  # asc升序，desc降序
                },
                "like_frequency": {  # 根据age字段升序排序
                    "order": "desc"  # asc升序，desc降序
                }
            }
        }

    data = es.search(index='video', doc_type='video', body=body)
    cache_hits = data['hits']['hits']
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