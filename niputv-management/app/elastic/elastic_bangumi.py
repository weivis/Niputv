from app.elastic.elasticconfig import *
from datetime import datetime
import json

def query_admin_bangumilist_lianzai():
    body = {"size" : 50, 'query': {'term': {'status': 1 }}}
    data = es.search(index='bangumi', doc_type='bangumi', body=body)
    cache_hits = data['hits']['hits']
    out = [{
        'id': i['_id'],
        'cover': i['_source']['cover'],
        'name': i['_source']['name'],
        'uploads_week': i['_source']['uploads_week'],
        'video_statistics': i['_source']['video_statistics']
    }for i in cache_hits]
    return out

def query_bangumi_data(id):
    if (id):
        data = es.get(index='bangumi', doc_type='bangumi', id=id)
        if (data):
            return data
        else:
            return ''
    else:
        return 'error:no id'

def change_bangumi_data(id,sort, info, cv, name):
    print(sort, info, cv, name)
    body={
        "doc": {
            'cv': cv,
            'introduction': info,
            'video_statistics': int(sort),
            'name': name
        }
    }
    es.update(index='bangumi', doc_type='bangumi', id=id, body=body)

def reg_bangumitag(tag,vid):
    cachedata = es.index(index="bangumi_tag", doc_type='bangumi_tag', body={
        'tag':tag,
        'bangumi_id':vid,
        'timestamp': datetime.now(), #排序日期
    })
    es.indices.refresh(index="bangumi_tag")

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
    out = [{
        'dataid': i['_id'],
        'tag': i['_source']['tag']
    }for i in data['hits']['hits']]
    return out