__author__ = 'Ran'
from app import Flask, cache, login_manager
from ..index import index
from app.account import Account
from flask_login import current_user, login_required
from flask import render_template, request, session, redirect
from app.elastic.elastic_query import get_onevideo_data
from app.Database.db_space import Space_userpg, Space_pg_video
import json

#indexpgvideo
@index.route('/indexpgvideo/<pgid>', methods=["POST"])
def Get_userpg_video(pgid):
	data = Space_pg_video.query.filter_by(pgid=pgid).all()
	jsondata = [{
	'videoid':data.videoid,
	'title': get_onevideo_data(data.videoid)['video_name'],
	'cover': get_onevideo_data(data.videoid)['video_cover'],
	}for data in data]
	return json.dumps(jsondata)

#用户资料api
@index.route('/getuservideopg/<userid>', methods=["POST"])
def Get_uservideo_pg(userid):
	data = Space_userpg.query.filter_by(id=userid).all()
	jsondata = [{
	'pgid':int(data.id),
	'title':data.pgname,
	'pginfo':data.pginfo,
	'pgvideoqu':data.pg_videopcs_statistics,
	}for data in data]
	return json.dumps(jsondata)

#用户资料api
@index.route('/getindexpglist/<pgid>', methods=["POST"])
def Get_index_pgvideolist(videoid):
	data = get_onevideo_data(videoid)
	return json.dumps(data)

#用户资料api
@index.route('/getvideo/<videoid>', methods=["POST"])
def Get_video(videoid):
	data = get_onevideo_data(videoid)
	return json.dumps(data)

#用户资料api
@index.route('/getinfo/<userid>', methods=["POST"])
def Get_info(userid):
	data = Account.query.filter_by(id=userid).first()
	outjson = {
	'username':data.username,
	'introduction':data.introduction,
	'head':data.head,
	'fan':data.fan_statistics,
	'play':data.play_quantity,
	'space_introduction':data.space_introduction,
	'topping_video':data.topping_video,
	}
	return json.dumps(outjson)

#首页
@index.route('/<int:userid>')
def home(userid):
	return render_template('space/index.html',data=json.dumps({"cache":int(userid)}))