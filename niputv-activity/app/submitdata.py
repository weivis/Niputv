#执行提交数据倒数据库
from sql import auth_playrecording_exist, write_playrecording, auth_playrecording_exist_bangumi, write_playrecording_bangumi
from video import video_playcount, del_redis_rs_data, get_videoalldata_rs, video_getall_count, del_redis_count_data
from bangumi import bangumi_playcount, del_redis_bangumi_line_data, get_bangumialldata_bangumi_line, del_redis_bangumicount_data, bangumi_getall_count
from elastic import up_videoplay_count, up_bangumiplay_count
import json

#get_videoalldata_rs() 获取视频列队表全部列队记录
#auth_playrecording_exist() ip是否已经播放过视频 检验函数
#write_playrecording()  写入一条这个ip已经看过这个视频的记录
#video_playcount() 统计对特定视频id叠加数据

def write_video_data():
    for i in get_videoalldata_rs():
        #取出单条数据 {"vid": "14.152.94.95-205848", "count": "{\"ip\": \"14.152.94.95\", \"vid\": \"AWan2vUPIFnsUJpxH6A2\"}"}
        jsondata = json.loads(i['data'])

        #获取ip记录
        authdata = auth_playrecording_exist(ip=jsondata['ip'],vid=jsondata['vid']) #检验这个ip 是否已经看国过这个vid
        #验证该ip是否已经播放过该视频
        if authdata == True:
            #print('数据存在 不写入数据库')
            pass

        else:
            #print('数据不存在 写入数据库')
            write_playrecording(ip=jsondata['ip'],vid=jsondata['vid'])
            #统计视频播放量
            video_playcount(jsondata['vid'])

        #删除rs表的指定统计记录
        del_redis_rs_data(i['key'])
        #print('删除缓存',i['key'])

    #执行完for后进行提交
    storage_video_elastic()

def storage_video_elastic():
    #取出已经统计好的数据
    data = video_getall_count()
    #循环逐条写入
    for i in data:
        #提交倒elastic（视频id 统计数量）
        up_videoplay_count(i['vid'],i['count'])
        del_redis_count_data(i['vid'])

#get_bangumialldata_bangumi_line() 获取全部番剧列队
#auth_playrecording_exist_bangumi() 检查这个ip是否已经看过这个视频

def write_bangumi_data():
    for i in get_bangumialldata_bangumi_line():
        #取出单条数据 {\"vid\": \"14.152.94.94-213803\", \"count\": \"{\\\"ip\\\": \\\"14.152.94.94\\\", \\\"vid\\\": \\\"1\\\"}\"}
        jsondata = json.loads(i['data'])

        #获取ip记录
        authdata = auth_playrecording_exist_bangumi(ip=jsondata['ip'],vid=jsondata['vid']) #检验这个ip 是否已经看国过这个vid
        #验证该ip是否已经播放过该视频
        if authdata == True:
            #print('数据存在 不写入数据库')
            pass

        else:
            #print('数据不存在 写入数据库')
            write_playrecording_bangumi(ip=jsondata['ip'],vid=jsondata['vid'])
            #统计视频播放量
            bangumi_playcount(jsondata['vid'])

        #删除rs表的指定统计记录
        del_redis_bangumi_line_data(i['key'])
    
    #执行完for后执行
    storage_bangumi_elastic()

def storage_bangumi_elastic():
    #取出已经统计好的数据
    data = bangumi_getall_count()
    #循环逐条写入
    for i in data:
        #提交倒elastic（视频id 统计数量）
        up_bangumiplay_count(i['vid'],i['count'])
        del_redis_bangumicount_data(i['vid'])
