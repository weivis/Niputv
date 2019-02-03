__author__ = 'Ran'
from app import Flask
from ..review import review
from app.account import Account
from flask import render_template
import json

from app.elastic.elastic_video import elastic_query_review_videolist, elastic_getvideo
from app.elastic.elastic_operating import change_video_reviewtype
from app.Database.db_video_content_class import Partition, Category
from app.Database.db_videofile import Videofile


#等待审核的视频页面
@review.route('/review')
def review_video():
    return render_template('review/review-videolist.html', headernav_tab='review')

#等待审核的视频列表
@review.route('/api/review-videolist')
def review_Get_review_videolist():
    return json.dumps(elastic_query_review_videolist())

#审核页面
@review.route('/review-video/<id>')
def review_video_page(id):
    data=Videofile.query.filter_by(videoid = id).first()
    video = data.filekey
    fname = video.split(".")[0]
    return render_template('review/review-video.html', headernav_tab='review', videoid=id, video=fname)

#视频审核页面获取视频信息
@review.route('/review-video/api/get-videoinfo/<id>')
def review_video_getvideoinfo(id):
    data = elastic_getvideo(id)
    fq = Partition.query.filter_by(id = data['_source']['partition']).first()
    lm = Category.query.filter_by(id = data['_source']['category']).first()
    datalist = {
        'fq': fq.name,
        'lm': lm.name,
        'video_id': data['_id'],
        'video_name': data['_source']['video_name'],
        'video_introduction': data['_source']['video_introduction'],
        'cover': data['_source']['video_cover'],
        'reprint': data['_source']['reprint'],
        'release_date': data['_source']['release_date'],
        'release_time': data['_source']['release_time']
    }
    return json.dumps(datalist)

#通过审核
@review.route('/review-video/api/review-operating/ok/<id>')
def review_video_videoreviewok(id):
    if (id):
        change_video_reviewtype(id=id, ctype=0)
        return json.dumps({"code":"ok"})
    else:
        return 'ERROR'