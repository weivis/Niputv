from app.elastic.elastic_tag import reg_videotag
from app.elastic.elastic_config import *

#注册视频tag
def write_Atag(tag,vid):
    data = es.get(index='video', doc_type='video', id=vid)
    if (data):
        if (tag):
                reg_videotag(tag,vid)
    else:
        return False