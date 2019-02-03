from app.elastic.elasticconfig import *

def elastic_query_review_videolist():
    body = {"size" : 30, 'query': {'term': {'status': 1 }}}
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

def elastic_getvideo(id):
    if (id):
        data = es.get(index='video', doc_type='video', id=id)
        if (data):
            return data
        else:
            return ''
    else:
        return 'error:no id'