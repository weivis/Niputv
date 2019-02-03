from app.elastic.elastic_config import *
from datetime import datetime

def reg_videotag(tag,vid):
    cachedata = es.index(index="tag", doc_type='tag', body={
        'tag':tag,
        'vid':vid,
        'timestamp': datetime.now(), #排序日期
    })
    es.indices.refresh(index="tag")

def get_videoalltag(vid):
    '''
    body = {
        "size" : 10,
        "query": {
            "bool": {
            "must": [
                { "match": { "vid": vid }}
            ]
            }
        },
        "sort": {
            "timestamp": {  # 根据age字段升序排序
                "order": "desc"  # asc升序，desc降序
            }
        }
    }
    '''
    body = {
        "size" : 10,
        "query": {
            "bool": {
            "must": [
                { "match": { "vid": vid }}
            ]
            }
        }
    }
    data = es.search(index='tag', doc_type='tag', body=body)
    out = [{'dataid': i['_id'], 'tag': i['_source']['tag']}for i in data['hits']['hits']]
    return out

def get_bangumialltag(id):
    body = {
        "size" : 10,
        "query": {
            "bool": {
            "must": [
                { "match": { "bangumi_id": id }}
            ]
            }
        }
    }
    data = es.search(index='bangumi_tag', doc_type='bangumi_tag', body=body)
    out = [{'dataid': i['_id'], 'tag': i['_source']['tag']}for i in data['hits']['hits']]
    return out