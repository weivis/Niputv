import redis
import time
import json

#bangumi 视频统计请求列队表
bangumi_line=redis.Redis(host='127.0.0.1', port=6379, db=2, decode_responses=True)

#bangumicount 番剧播放量统计表
bangumicount=redis.Redis(host='127.0.0.1', port=6379, db=4, decode_responses=True)

def get_bangumialldata_bangumi_line():
    data = bangumi_line.keys()
    alist = []
    for i in data:
        data = bangumi_line.get(i)
        jsondata = {"key":i,"data":data}
        alist.append(jsondata)
    return alist

def bangumicount_viewsdataget_count():
    data = bangumicount.keys()
    alist = []
    for i in data:
        data = bangumicount.get(i)
        jsondata = {"key":i,"val":data}
        alist.append(jsondata)
    return alist

def bangumi_viewsdataget_bangumi_line():
    data = bangumi_line.keys()
    alist = []
    for i in data:
        data = bangumi_line.get(i)
        jsondata = {"vid":i,"count":data}
        alist.append(jsondata)
    return alist

#count 视频播放量统计表增加播放记录操作{vid:视频id,viddata = 统计的结果}
def bangumi_playcount(vid):

    #获取vid的值(vid=videoid, val=vid(val))
    viddata = bangumicount.get(vid)

    #查询vid是否存在
    if viddata:

        #存在 (获取vid，设置值 + 1)
        bangumicount.getset(vid, viddata + 1)

    else:
        #不存在播放数量(设置该vid=1)
        bangumicount.set(vid, 1)

#验证key是否重复
def auth_bangumi_key(uid):
    if bangumi_line.get(uid):
        return False
    else:
        return True

#写入番剧播放记录
def write_bangumi_playrecording(ip, video_id):
    gid = ip + '-' + time.strftime("%H%M%S", time.localtime())
    if auth_bangumi_key(gid):
        jsonlist = {
            "ip":ip,
            "vid":video_id
        }
        jsonlist = json.dumps(jsonlist)
        bangumi_line.set(gid,jsonlist)

#[写入数据库用]删除视频统计表指定数据(rs)
def del_redis_bangumi_line_data(key):
    bangumi_line.delete(key)

#[写入数据库用]删除视频统计表指定数据(rs)
def del_redis_bangumicount_data(key):
    bangumicount.delete(key)

#获取已经统计了的视频的播放量数据(vid,val) 并返回列表
def bangumi_getall_count():
    data = bangumicount.keys()
    alist = []
    for i in data:
        data = bangumicount.get(i)
        jsondata = {"vid":i,"count":data}
        alist.append(jsondata)
    return alist