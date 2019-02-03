from flask_login import current_user
from app.elastic.elastic_config import *
import time
from datetime import datetime

def upadd_commentpcs(videoid):
    videodata = es.get(index='video', doc_type='video', id=videoid)
    body={
        "doc": {
            'comment_statistics': videodata['_source']['comment_statistics'] + 1
        }
    }
    es.update(index='video', doc_type='video', id=videoid, body=body)


def video_likeadd(videoid, settype, settype2):
    videodata = es.get(index='video', doc_type='video', id=videoid)
    print(videodata)
    if settype == True:
        if settype2 == 'add':
            body={
                "doc": {
                    'like_frequency': videodata['_source']['like_frequency'] + 1
                }
            }

        elif settype2 == 'del':
            body={
                "doc": {
                    'like_frequency': videodata['_source']['like_frequency'] - 1
                }
            }
    elif settype == False:
        if settype2 == 'add':
            body={
                "doc": {
                    'dislike_frequency': videodata['_source']['dislike_frequency'] + 1
                }
            }

        elif settype2 == 'del':
            body={
                "doc": {
                    'dislike_frequency': videodata['_source']['dislike_frequency'] - 1
                }
            }
    es.update(index='video', doc_type='video', id=videoid, body=body)