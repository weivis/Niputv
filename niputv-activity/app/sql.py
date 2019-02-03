# coding: utf-8
import pymysql
import time

#查找该部番剧的id
def getbangumivideo_bangumiid(id):
    db=pymysql.connect(host="localhost",user="root", password="", db="niputv",port=3307, charset='utf8')
    cursor = db.cursor()
    #print('查询数据是否存在数据库>ip:',ip,' - vid:',vid)
    results=cursor.execute("select bangumi_id from bangumi_video where id=%s",(id))
    data = cursor.fetchone()
    db.commit()
    db.close()
    return data

#验证该ip是否已经观看过这个视频
def auth_playrecording_exist(ip, vid):
    db=pymysql.connect(host="localhost",user="root", password="", db="niputv-activity",port=3307, charset='utf8')
    cursor = db.cursor()
    #print('查询数据是否存在数据库>ip:',ip,' - vid:',vid)
    results=cursor.execute("select ip,vid from playrecording where ip=%s and vid=%s",(ip,vid))
    db.commit()
    db.close()
    if results:
        return True
    else:
        return False

#写入这个ip已经观看了这个视频的记录
def write_playrecording(ip, vid):
    db=pymysql.connect(host="localhost",user="root", password="", db="niputv-activity",port=3307, charset='utf8')
    cursor = db.cursor()
    sql = "insert into playrecording(ip, vid) values('%s', '%s');" % (ip, vid)
    cursor.execute(sql)
    db.commit()

#验证该ip是否已经观看过这个视频
def auth_playrecording_exist_bangumi(ip, vid):
    db=pymysql.connect(host="localhost",user="root", password="", db="niputv-activity",port=3307, charset='utf8')
    cursor = db.cursor()
    #print('查询数据是否存在数据库>ip:',ip,' - vid:',vid)
    results=cursor.execute("select ip,vid from playbangumi_recording where ip=%s and vid=%s",(ip,vid))
    db.commit()
    db.close()
    if results:
        return True
    else:
        return False

#写入这个ip已经观看了这个视频的记录
def write_playrecording_bangumi(ip, vid):
    db=pymysql.connect(host="localhost",user="root", password="", db="niputv-activity",port=3307, charset='utf8')
    cursor = db.cursor()
    sql = "insert into playbangumi_recording(ip, vid) values('%s', '%s');" % (ip, vid)
    cursor.execute(sql)
    db.commit()