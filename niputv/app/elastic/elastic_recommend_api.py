from app.elastic.elastic_config import *
from app.middleware.get_cacheuser import get_middleware_account

def get_videoname_relatedvideo(video_name):
    '''
    data = es.search(index="video", doc_type='video', body={
        'size': 5,
        'query': {
            'match': {
                'video_name': video_name,
                }
            }
        })
    '''
    data = es.search(index="video", doc_type='video', body={
        'size': 20,
        'query': {
            'match': {'status': 0},
        }
    }
    )
    cache_hits = data['hits']['hits']
    out = [{
        'video_id': i['_id'],
        'video_name': i['_source']['video_name'],
        'video_cover': i['_source']['video_cover'],
        'release_date': i['_source']['release_date'],
        'play_statistics': i['_source']['play_statistics'],
        'upusername': (get_middleware_account(i['_source']['authorid'])).username,
    }for i in cache_hits]
    return out