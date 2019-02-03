from app.elastic.elastic_config import *

def get_onevideo_data(id):
	i = es.get(index='video', doc_type='video', id=id)
	data = {
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
	}
	return data