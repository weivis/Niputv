__author__ = 'Ran'
from app import Flask, cache, login_manager, db
from ..bangumi import bangumi
from app.account import Account
from flask_login import current_user, login_required
from flask import render_template, request, session, redirect
import json
import time
import hashlib

from app.cloud import Get_coverupload_token, bangumi_cover_transcoding, Get_UploadToken, generate_videoabbreviation_cover, del_bangumivideo_filekey, del_bangumi_cover
from app.elastic.elastic_bangumi import query_admin_bangumilist_lianzai, query_bangumi_data, change_bangumi_data
from app.elastic.elastic_operating import create_newbangumi, uploads_bangumi_shelf, uploads_bangumi_status, es_del_bangumi, change_bangumi_videopcs

from app.Database.db_videofile import Bangumi_video
from app.transcoding import continuous_video_transcoding

from app.bangumi.tag import write_tag
from app.elastic.elastic_bangumi import get_bangumialltag

#------------------------------------------------------------------------------------------------------------------------------

@bangumi.route('/api/get/bangumi/tag/id/<id>')
def get_bangumi_alltag(id):
    data = get_bangumialltag(id)
    return json.dumps(data)

#----------------------------------------------------番剧发布-和其他索引页-------------------------------------------------------

#连载中
@bangumi.route('/loading')
def bangumi_loading():
    return render_template('bangumi/bangumi-loading.html', headernav_tab='bangumi', features_tab='bangumi-loading')

#连载中-列表接口
@bangumi.route('/loading/api/get-list')
def bangumi_loading_Getlist():
    return json.dumps(query_admin_bangumilist_lianzai())

#发布新的番剧
@bangumi.route('/release')
def bangumi_release():
    return render_template('bangumi/bangumi-release.html', headernav_tab='bangumi', features_tab='bangumi-release')

#番剧封面上传许可证
@bangumi.route('/release/api/get-coverupload-token/<filename>', methods=["GET", "POST"])
def bangumi_get_coverupload_token(filename):
    if (filename):
        newkey = time.strftime("%Y%m%d%H%M%S", time.localtime())
        filetype = filename.split('.')[-1]

        generate_key = newkey +'.'+ filetype
        data = Get_coverupload_token(bucket_name='cover-cache', key=generate_key, outtime='3600')
        if(data):
            print(generate_key)
            return json.dumps({'token': data, 'key': generate_key})

#接收发布的新番剧接口
@bangumi.route('/release/api/push', methods=["POST"])
def bangumi_release_api():
    jsondata = request.json
    bangumi_name = jsondata['bangumi_name']
    bangumi_nianfen = jsondata['bangumi_nianfen']
    bangumi_playtype = jsondata['bangumi_playtype']
    bangumi_uploads_wk = jsondata['bangumi_uploads_wk']
    bangumi_uploads_time = jsondata['bangumi_uploads_time']
    bangumi_cv = jsondata['bangumi_cv']
    bangumi_infos = jsondata['bangumi_infos']
    bangumi_cover = jsondata['bangumi_cover']
    bangumi_month = jsondata['month']

    if bangumi_playtype == 1 or 2:
        bangumi_playtype = bangumi_playtype
    else:
        return 'error'
    if bangumi_cover == None or '':
        return 'error'
    else:
        bangumiid = create_newbangumi(name = bangumi_name,year = bangumi_nianfen,month=bangumi_month,status = bangumi_playtype, uploads_week = bangumi_uploads_wk,uploads_time=bangumi_uploads_time,cv=bangumi_cv,introduction=bangumi_infos, cover = bangumi_cover)
        write_tag(tag=jsondata['bangumi_tag'], vid=bangumiid)
        bangumi_cover_transcoding(key = bangumi_cover , sizi = None)
        bangumi_cover_transcoding(key = bangumi_cover, sizi = 'min')
        return json.dumps({'code':'ok'})


#编辑-输入番剧id
@bangumi.route('/edit')
def bangumi_edit():
    return render_template('bangumi/bangumi-edit_302.html', headernav_tab='bangumi', features_tab='bangumi-edit')

#----------------------------------------------------番剧编辑-------------------------------------------------------

#编辑-番剧信息页面
@bangumi.route('/edit/<id>')
def bangumi_edit_info(id):
    return render_template('bangumi/bangumi-edit.html', headernav_tab='bangumi', features_tab='bangumi-edit', bangumiid = id)

#编辑-番剧信息接口
@bangumi.route('/edit/api/id/<id>')
def bangumi_edit_bangumiinfoget(id):
    data = query_bangumi_data(id)
    datalist = {
        'id':data['_id'],
        'name':data['_source']['name'],
        'year': data['_source']['year'],
        'month': data['_source']['month'],
        'status': data['_source']['status'],
        'cover': data['_source']['cover'],
        'uploads_week': data['_source']['uploads_week'],
        'uploads_time': data['_source']['uploads_time'],
        'cv': data['_source']['cv'],
        'introduction': data['_source']['introduction'],
        'play_statistics': data['_source']['play_statistics'],
        'sub_statistics': data['_source']['sub_statistics'],
        'like_frequency': data['_source']['like_frequency'],
        'dislike_frequency': data['_source']['dislike_frequency'],
        'creation_time': data['_source']['creation_time'],
        'video_statistics': data['_source']['video_statistics'],
        'shelf': data['_source']['shelf'],
        'tag': get_bangumialltag(id)
    }
    return json.dumps(datalist)

#编辑-上下架番剧
@bangumi.route('/edit/api/shelf/<id>/<shelftype>')
def bangumi_shelf_change(id, shelftype):
    if shelftype == 0 or 1:
        uploads_bangumi_shelf(id,shelftype)
        return json.dumps({'code':'ok'})
    return json.dumps({'code':'error'})

#编辑-完结番剧
@bangumi.route('/edit/api/status/<id>/<shelftype>')
def bangumi_status_change(id, shelftype):
    if shelftype == 0 or 1:
        uploads_bangumi_status(id,shelftype)
        return json.dumps({'code':'ok'})
    return json.dumps({'code':'error'})

#编辑-删除番剧
@bangumi.route('/edit/api/del/<id>')
def bangumi_delbangumi(id):
    bangumidata = query_bangumi_data(id)
    es_del_bangumi(id)
    del_bangumi_cover(bangumidata['_source']['cover'])
    del_bangumi_cover('20181104064150.jpg')
    data = Bangumi_video.query.filter_by(bangumi_id=id).all()
    for i in data:
        del_bangumivideo_filekey(i.filekey)
    return json.dumps({'code':'ok'})

#----------------------------------------------------番剧编辑-修改番剧资料-------------------------------------------------------

@bangumi.route('/edit/data/<id>', methods=["GET", "POST"])
def bangumidata_deit(id):
    if request.method == 'POST':
        jsondata = request.json
        change_bangumi_data(id=id,sort=jsondata['sort'], info=jsondata['info'], cv=jsondata['cv'], name=jsondata['name'])
        return json.dumps({'code':'200'})
    else:
        return render_template('bangumi/bangumi-bangumidataedit.html', headernav_tab='bangumi', features_tab='bangumi-edit', bangumiid = id)

#----------------------------------------------------番剧编辑-管理剧集-------------------------------------------------------

#编辑-剧集管理
@bangumi.route('/edit/drama/<id>')
def bangumi_edit_drama(id):
    return render_template('bangumi/bangumi-dramaedit.html', headernav_tab='bangumi', features_tab='bangumi-edit')

#编辑-剧集管理-api-获取剧集
@bangumi.route('/edit/drama/api/get-dramalist/<id>')
def bangumi_edit_getdramalist(id):
    data = Bangumi_video.query.filter_by(bangumi_id=id).all()
    jsondata = [{
        'id': i.id,
        'video_name': i.video_name,
        'video_sort': i.video_sort,
        'cover': i.cover,
        'time': i.upload_date
    }for i in data]
    return json.dumps(sorted(jsondata, key=lambda x:int(x['video_sort']), reverse=True))

#编辑-剧集管理
@bangumi.route('/edit/drama/video/<id>')
def bangumi_edit_drama_video(id):
    return render_template('bangumi/bangumi-dramaedit.html', headernav_tab='bangumi', features_tab='bangumi-edit')

#----------------------------------------------------番剧编辑-上传剧集-------------------------------------------------------

#编辑-上传剧集
@bangumi.route('/edit/drama/upload/<id>')
def bangumi_upepisode(id):
    return render_template('bangumi/bangumi-dramaeupload.html', headernav_tab='bangumi')

#上传番剧的许可证
@bangumi.route('/edit/drama/upload/api/video-token', methods=["GET", "POST"])
def upload_token():
    filename = request.args.get('filename')
    filetype = filename.split(".")[-1]
    if filetype == 'mp4' or filetype == 'mkv' or 'flac':
        md5key = (hashlib.md5((current_user.user_email).encode()).hexdigest()) + time.strftime("%H%M%S", time.localtime())
        generate_key = md5key + '.' + filetype
        data = Get_UploadToken(bucket_name='video-cache', key=generate_key, outtime=(60*60)*20)
        return json.dumps({'token': data, 'key': generate_key, 'filename': filename, 'filetype': filetype, 'coverkey': md5key, 'code':0})
    else:
        return json.dumps({'code':1})

#上传番剧的许可证
@bangumi.route('/edit/drama/upload/api/push', methods=["GET", "POST"])
def upload_upload_push():
    file_key = request.form.get('file_key')
    bangumi_id = request.form.get('bangumi_id')
    drama_name = request.form.get('drama_name')
    drama_sort = request.form.get('drama_sort')

    if file_key == '':
        return json.dumps({'code':'error', 'text':'视频不存在'})

    if drama_name == '':
        return json.dumps({'code':'error', 'text':'所属番剧不存在'})

    if drama_sort == '':
        return json.dumps({'code':'error', 'text':'话数不能为空'})

    if Bangumi_video.query.filter_by(bangumi_id=bangumi_id, video_sort=drama_sort).first():
        text = '第' + drama_sort + '话已存在'
        return json.dumps({'code':'error', 'text':text})

    key = file_key.split(".")[0]
    cover = generate_videoabbreviation_cover(coverkey = key, videokey=file_key)
    continuous_video_transcoding(key = file_key, bangumi_id=bangumi_id, cover=cover, videoname=drama_name, videosort=drama_sort)
    change_bangumi_videopcs(id=bangumi_id, ctype='up')
    return json.dumps({'code':'ok'})