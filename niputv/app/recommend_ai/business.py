from app.elastic.elastic_recommend_api import get_videoname_relatedvideo

def get_recommend_videolist(upid, videoname):
    data = get_videoname_relatedvideo(videoname)
    return data