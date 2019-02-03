from app.elastic.elastic_bangumi import reg_bangumitag

#注册视频tag
def write_tag(tag,vid):
    if (tag):
        for i in tag:
            reg_bangumitag(i,vid)