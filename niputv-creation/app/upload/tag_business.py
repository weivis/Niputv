from app.elastic.elastic_tag import reg_videotag
from app.elastic.elastic_config import *

#注册视频tag
def write_tag(tag,vid):
    if (tag):
        for i in tag:
            reg_videotag(i,vid)