from app.elastic.elastic_config import *

def es_query_video(id):
    if (id):
        data = es.get(index='video', doc_type='video', id=id)
        if (data):
            return data
        else:
            return ''
    else:
        return 'error:no id'
    
def es_query_bangumi(id):
    if (id):
        data = es.get(index='bangumi', doc_type='bangumi', id=id)
        if (data):
            return data
        else:
            return ''
    else:
        return 'error:no id'