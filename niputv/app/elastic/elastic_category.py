from app.elastic.elastic_config import *
from app.Database.db_global import Category

'''
age = 升序
desc = 降序
min 按照该字段最小值排序
max 按照该字段最大值进行排序
avg 按照多个字段平均值排序
sum 按照字段总和进行排序
'''


def get_category_videolist(category_name, sort_type, pagination):
    #print(category_name, sort_type, pagination)

    #通过url名查询对应类目取出id
    getdata = Category.query.filter_by(subcategory_url = category_name).first()

    #判断是否存在
    if (getdata):
        category_id = getdata.id
        #print(category_id)

        #页数
        getpage = int(pagination) * 10

        #正常
        if sort_type == 'normal':
            body = {
                "from" : getpage, "size" : 10,
                "query": {
                    "bool": {
                    "must": [
                        { "match": { "category": category_id }},
                        { "match": { "status": 0 }}
                    ]
                    }
                },
                "sort": {
                    "timestamp": {
                        "order": "desc"
                    }
                }
            }

        elif sort_type == 'play':
            body = {
                "from" : getpage, "size" : 10,
                "query": {
                    "bool": {
                    "must": [
                        { "match": { "category": category_id }},
                        { "match": { "status": 0 }}
                    ]
                    }
                },
                "sort": {
                    "play_statistics": {  # 根据age字段升序排序
                        "order": "desc"  # asc升序，desc降序
                    }
                }
            }

        elif sort_type == 'like':
            body = {
                "from" : getpage, "size" : 10,
                "query": {
                    "bool": {
                    "must": [
                        { "match": { "category": category_id }},
                        { "match": { "status": 0 }}
                    ]
                    }
                },
                "sort": {
                    "like_frequency": {  # 根据age字段升序排序
                        "order": "desc"  # asc升序，desc降序
                    }
                }
            }
        #print(body)
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

    else:
        return 'error'

def get_category_videoclass(id):

        body = {
            "size" : 10,
            "query": {
                "bool": {
                "must": [
                    { "match": { "category": id }},
                    { "match": { "status": 0 }}
                ]
                }
            },
            "sort": {
                "timestamp": {
                    "order": "desc"
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