from app.elastic.elastic_config import *
from datetime import datetime

def reg_videotag(tag,vid):
    cachedata = es.index(index="tag", doc_type='tag', body={
        'tag':tag,
        'vid':vid,
        'timestamp': datetime.now(), #排序日期
    })
    es.indices.refresh(index="tag")

def get_video_alltag(id):
    body = {
        "size":10,
        "query": {
            "bool": {
            "must": [
                { "match": { "vid": id }}
            ]
            }
        }
    }
    data = es.search(index='tag', doc_type='tag', body=body)
    out = [{'tagid': i['_id'], 'tag': i['_source']['tag']}for i in data['hits']['hits']]
    return out

def video_all_tag(id):
	data = get_video_alltag(id)
	for i in data:
		es.delete(index='tag', doc_type='tag', id=i['tagid'])