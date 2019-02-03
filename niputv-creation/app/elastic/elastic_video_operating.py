from flask_login import current_user
from app.elastic.elastic_config import *
import time
from datetime import datetime
from app.cloud import del_video_cover

#生成视频稿件
def create_newvidoe(partition, category, grade_4k, video_cover, video_name, video_introduction, video_reprint):
    cachedata = es.index(index="video", doc_type='video', body={
        'partition': partition, #视频分区
        'category': category, #视频类目
        'authorid': current_user.id, #作者id
        'grade_4k': grade_4k, #4k条件 0=无 1=有
        'release_date': time.strftime("%Y-%m-%d",time.localtime(time.time())), #发布日期
        'release_time': time.strftime('%H:%M:%S',time.localtime(time.time())), #时间
        'timestamp': datetime.now(), #排序日期
        'status': 1, #视频状态 0=正常 1=未审核 2=退回
        'video_cover': video_cover, #视频封面
        'video_name': video_name, #视频名
        'video_introduction': video_introduction, #视频介绍
        'video_duration': '', #视频时长
        'reprint': video_reprint, #视频转载地址(无地址=原创)
        'play_statistics': 0, #播放数统计
        'comment_statistics': 0, #评论数统计
        'like_frequency': 0, #喜欢统计
        'dislike_frequency': 0, #不喜欢统计
    })
    es.indices.refresh(index="video")
    return cachedata['_id']

#写入视频信息(视频id 传入值 视频清晰度 视频是否开启4K转码模式)
def write_videomain(videoid, video_duration, grade_4k):
    if grade_4k == True:
        grade_4k = 1
    else:
        grade_4k = 0
    es.update(index='video', doc_type='video', id=videoid, body={
        "doc": {
            'video_duration': video_duration,
            'grade_4k': grade_4k
        }
    })

def es_del_video(id):
    #删除封面
    video = es.get(index='video', doc_type='video', id=id)
    del_video_cover(video['_source']['video_cover'])
    try:
        es.delete(index='video', doc_type='video', id=id)
        return 'ok'
    except:
        return 'no video id'

def es_query_video(id):
    if (id):
        data = es.get(index='video', doc_type='video', id=id)
        if (data):
            return data
        else:
            return ''
    else:
        return 'error:no id'