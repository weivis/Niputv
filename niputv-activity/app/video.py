import redis
import time
import json

#rs 视频统计请求列队表
rs=redis.Redis(host='127.0.0.1', port=6379, db=0, decode_responses=True)

#count 视频播放量统计表
count=redis.Redis(host='127.0.0.1', port=6379, db=1, decode_responses=True)

def get_videoalldata_rs():
    data = rs.keys()
    alist = []
    for i in data:
        data = rs.get(i)
        jsondata = {"key":i,"data":data}
        alist.append(jsondata)
    return alist

def video_viewsdataget_rs():
    data = rs.keys()
    alist = []
    for i in data:
        data = rs.get(i)
        jsondata = {"vid":i,"count":data}
        alist.append(jsondata)
    return alist

def video_viewsdataget_count():
    data = count.keys()
    alist = []
    for i in data:
        data = count.get(i)
        jsondata = {"key":i,"val":data}
        alist.append(jsondata)
    return alist

#验证key是否重复
def auth_video_key(uid):
    if rs.get(uid):
        return False
    else:
        return True

#写入视频播放记录
def write_video_playrecording(ip, video_id):
    gid = ip + '-' + time.strftime("%H%M%S", time.localtime())
    if auth_video_key(gid):
        jsonlist = {
            "ip":ip,
            "vid":video_id
        }
        jsonlist = json.dumps(jsonlist)
        rs.set(gid,jsonlist)

#count 视频播放量统计表增加播放记录操作{vid:视频id,viddata = 统计的结果}
def video_playcount(vid):

    #获取vid的值(vid=videoid, val=vid(val))
    viddata = count.get(vid)

    #查询vid是否存在
    if viddata:

        #存在 (获取vid，设置值 + 1)
        count.getset(vid, viddata + 1)

    else:
        #不存在播放数量(设置该vid=1)
        count.set(vid, 1)

#[写入数据库用]删除视频统计表指定数据(rs)
def del_redis_rs_data(key):
    rs.delete(key)

#获取已经统计了的视频的播放量数据(vid,val) 并返回列表
def video_getall_count():
    data = count.keys()
    alist = []
    for i in data:
        data = count.get(i)
        jsondata = {"vid":i,"count":data}
        alist.append(jsondata)
    return alist

#[写入数据库用]删除视频统计表指定数据(rs)
def del_redis_count_data(key):
    count.delete(key)