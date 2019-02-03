from elasticsearch import Elasticsearch
from sql import getbangumivideo_bangumiid
es = Elasticsearch([{u'host': u'127.0.0.1', u'port': 9201}])

#更新指定商品id的统计数据（videoid, 追加统计数量）
def up_videoplay_count(videoid, count):
    try:
        videodata = es.get(index='video', doc_type='video', id=videoid)
        body={
            "doc": {
                'play_statistics': videodata['_source']['play_statistics'] + int(count) #在元数据上+新的统计结果更新倒视频上
            }
        }
        es.update(index='video', doc_type='video', id=videoid, body=body)
    except:
        pass

#更新指定商品id的统计数据（videoid, 追加统计数量）
def up_bangumiplay_count(videoid, count):
    bangumiid = getbangumivideo_bangumiid(videoid)
    try:
        videodata = es.get(index='bangumi', doc_type='bangumi', id=bangumiid)
        body={
            "doc": {
                'play_statistics': videodata['_source']['play_statistics'] + int(count) #在元数据上+新的统计结果更新倒视频上
            }
        }
        es.update(index='bangumi', doc_type='bangumi', id=bangumiid, body=body)
    except:
        pass