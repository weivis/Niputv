__author__ = 'Ran'
from app import Flask, cache, login_manager
from ..upload import upload
from app.account import Account
from flask_login import current_user, login_required
from flask import render_template, request, session, redirect

from app.elastic.elastic_video_operating import create_newvidoe
from app.Database.db_global import Category, Partition
from app.cloud import Get_uploadtoken, Generate_video_cover, cover_transcoding
from app.video.video_continuous import continuous_video_transcoding, write_videoinfo
from app.upload.tag_business import write_tag
from app.Database.db_global import upload_category_upcount
import json
import time
import hashlib

VIDEOFILE_TYPE = ["flv","mp4"]
COVERFILE_TYPE = ["png","jpg","jpeg","gif"]

#首页
@upload.route('/')
@login_required
def upload_home():
    return render_template('creation/upload.html',title="发布作品")

#获取封面上传许可证
@upload.route('/cover-upload-token', methods=["GET", "POST"])
@login_required
def get_video_cover_upload_token():
    '''
        提取filename表单字段 filename 封面图源文件名
        提取key字段 key字段储存的是视频生成的key
    '''
    filename = request.args.get('filename')
    key = request.args.get('key')
    filetype = filename.split('.')[-1]
    
    if filetype in COVERFILE_TYPE : 
        #这一步很重要 如果key不存在表示用户未选择上传的文件 该情况下禁止上传封面图
        if (key):
            #生成新的封面图 key
            generate_key = str(key) + '.jpg'# + filetype
            data = Get_uploadtoken(bucket_name='cover-cache', key=generate_key, outtime='3600')
            print(generate_key)
            if(data):#判断token是否获取成功
                return json.dumps({'code':'ok', 'text':'成功获取封面图上传许可证', 'covertoken':data, 'filetype':filetype, 'key':generate_key})
            return json.dumps({'code':'no', 'text':'封面图许可证生成失败', 'covertoken':'', 'filetype':filetype})
        return json.dumps({'code':'no', 'text':'用户尚未上传视频文件 非法操作', 'covertoken':'', 'filetype':filetype})
    return json.dumps({'code':'no', 'text':'上传的文件类型不允许', 'covertoken':'', 'filetype':filetype})

#获取视频上传许可证
@upload.route('/video-upload-token', methods=["GET", "POST"])
@login_required
def get_video_file_upload_token():
    #获取filename字段内容 该字段储存的内容为文件名
    filename = request.args.get('filename')
    filetype = filename.split('.')[-1] #提取文件扩展名

    #判断是否允许上传的文件格式
    if filetype in VIDEOFILE_TYPE:
        #生成md5唯一key(用户邮箱+时间)
        md5key = (hashlib.md5((current_user.user_email).encode()).hexdigest()) + time.strftime("%H%M%S", time.localtime())
        #重新组合文件名
        generate_key = md5key + '.' + filetype
        #获取token
        data = Get_uploadtoken(bucket_name='video-cache', key=generate_key, outtime='8000') #此处使用完整key
        if(data):#判断token是否获取成功
            return json.dumps({'code':'ok', 'text':'成功获取视频上传许可证', 'uploadtoken':data, 'key':md5key, 'filetype':filetype}) #此处使用非完整key
        return json.dumps({'code':'no', 'text':'许可证生成失败', 'uploadtoken':'', 'filetype':filetype})
    return json.dumps({'code':'no', 'text':'上传了非法的文件', 'uploadtoken':'', 'filetype':filetype})

#获取主分区
@upload.route('/get_main_category', methods=["POST"])
@login_required
def get_main_category():
	data = Partition.query.filter().all()
	datalist = [{'id':str(i.id),'name':i.name}for i in data]
	print(datalist)
	return json.dumps(datalist)

#获取子分区
@upload.route('/get_sub_category', methods=["POST"])
@login_required
def get_sub_category():
	classid = request.args.get('classid')
	data = Category.query.filter_by(partition_id=classid, allow=0).all()
	datalist = [{"id":i.id,"name":i.name}for i in data]
	print(datalist)
	return json.dumps(datalist)

#发布视频
@upload.route('/release', methods=["POST"])
@login_required
def release_video():
    if request.method == 'POST':
        jsondata = request.json
        print(jsondata)
        if jsondata['video_title'] == '':
            return json.dumps({'code':'no', 'text':'视频名不能为空'})

        if jsondata['video_key'] == '':
            return json.dumps({'code':'no', 'text':'出现未知错误'})

        if jsondata['category'] == '':
            return json.dumps({'code':'no', 'text':'未选择分区或类目'})

        if jsondata['subdivision'] == '':
            return json.dumps({'code':'no', 'text':'未选择分区或类目'})

        if jsondata['video_introduction'] == '':
            return json.dumps({'code':'no', 'text':'视频介绍不能为空'})

        if jsondata['reprint'] == None or jsondata['reprint'] == '':
            reprint = ''
        else:
            reprint = jsondata['reprint']

        if jsondata['cover_key'] == '' or jsondata['cover_key'] == None:
            print('不存在缩略图')
            #不存在封面和上传类型
            coverkey = jsondata['video_key'].split(".")[0]
            #生成缩略图(返回的是生成的值)
            videocover = Generate_video_cover(coverkey=coverkey,videokey=jsondata['video_key'])

        else:
            if jsondata['covertype'] == True:
                #存在封面 存在上传类型
                cover_transcoding(key = jsondata['cover_key'])#压缩封面图生成缩略图
                videocover = jsondata['cover_key']

        #禁用4K
        grade_4k = '0'

        try:
            #发起持续化业务处理
            videodata = continuous_video_transcoding(key=jsondata['video_key'])

            #确保不存在问题后生成视频稿件(并返回id)
            videoid = create_newvidoe(partition=jsondata['category'], category=jsondata['subdivision'], grade_4k=grade_4k, video_cover=videocover, video_name=jsondata['video_title'], video_introduction=jsondata['video_introduction'], video_reprint=jsondata['reprint'])
            
            #print('vidoeid:',videoid)

            #tag处理业务
            write_tag(tag=jsondata['tag'], vid=videoid)

            write_videoinfo(videodata,videoid = videoid,k4 = grade_4k)

            upload_category_upcount(jsondata['subdivision'])

            return json.dumps({'code':'ok'})
        except:
            return json.dumps({'code':'no','text':'系统繁忙 请重试提交'})
            