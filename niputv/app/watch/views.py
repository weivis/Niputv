__author__ = 'Ran'
from app import Flask
from ..watch import watch
from flask import render_template, request, url_for, jsonify, redirect
from app.Database.db_video import Videofile
from app.elastic.elastic_global import es_query_video
import json


#首页
@watch.route('/<id>')
def video_play(id):
	video_data = get_videoinfo(id)
	video_file = False

	#获取视频数据 视频不存在返回False
	if(video_data == False):
		video_data = False

	#如果存在获取视频文件信息
	else:
		video_file = get_vidoefile(id)

	return render_template('watch/video_watch.html',info=json.dumps(video_data), key = json.dumps(video_file), title=video_data['video_name'], pagid=id)


#返回类型 dict
def get_videoinfo(id):
	try:
		data = es_query_video(id)
		list = {
			'video_id': data['_id'],
			'video_name': data['_source']['video_name'],
			'up': data['_source']['authorid'],
			'video_introduction': data['_source']['video_introduction'],
			'play_statistics': data['_source']['play_statistics'],
			'release_date': data['_source']['release_date'],
			'release_time': data['_source']['release_time'],
			'reprint': data['_source']['reprint'],
			'partition': data['_source']['partition'],
			'category': data['_source']['category'],
			'comment_statistics': data['_source']['comment_statistics'],
		}
		return list
	except:
		return False


#返回类型 dict
def get_vidoefile(id):
	videodata = Videofile.query.filter_by(videoid = id).first()

	if(videodata):
		data = {
			"key":videodata.filekey,
			"360":videodata.clear360,
			"480":videodata.clear480,
			"720":videodata.clear720,
			"1080":videodata.clear1080,
			"2k":videodata.clear2k,
			"4k":videodata.clear4k,
		}
	else:
		data = False

	return data