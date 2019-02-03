# -*- coding: utf-8 -*-
__author__ = 'Ran'
from app import Flask, db, cache
from ..category import category
from flask import render_template, request, url_for, jsonify, redirect
from app.Database.db_global import Region, Partition, Category
from app.elastic.elastic_category import get_category_videolist, get_category_videoclass
import json

#分区主页
@category.route('/<url>')
def category_home(url):
	data = Partition.query.filter_by(maincategory_url = url).first()

	#判断是否存在该分区
	if data == None or '':
		return 'URL有误'
	else:
		title = data.name
		get = Region.query.filter_by(partition_id = data.id).first()
		#判断是否存在分区风格参数
		if (get):
			jsondata = {
				'ico': get.ico,
				'cover': get.cover,
				'name_en': get.name_en,
				'name_cn': get.name_cn,
			}
		else:
			jsondata = {
				'ico': 'None',
				'cover': 'None',
				'name_en': 'None',
				'name_cn': 'None',
			}
		navdata = Category.query.filter_by(partition_id = data.id).all()

		nav = [{
			'id': i.id,
			'navtitle': i.name,
			'url': url+'/'+i.subcategory_url,
			'sort': i.sort,
		}for i in navdata]

		cahcedata = {'style': jsondata, 'nav': sorted(nav, key=lambda x:x['sort'], reverse=True)}
	return render_template('index/category-category.html',data=cahcedata, title=title)
	
#分区主页
@category.route('/<url>/<fq>')
def category_videolist(url,fq):
	#获取a
	data = Partition.query.filter_by(maincategory_url = url).first()
	
	#判断是否存在该分区
	if data == None or '':
		return 'URL有误'

	else:
		#获取url该分区的数据
		get = Region.query.filter_by(partition_id = data.id).first()
		if (get):
			jsondata = {
				'ico': get.ico,
				'cover': get.cover,
				'name_en': get.name_en,
				'name_cn': get.name_cn,
			}
		else:
			jsondata = {
				'ico': 'None',
				'cover': 'None',
				'name_en': 'None',
				'name_cn': 'None',
			}

		#nav
		navdata = Category.query.filter_by(partition_id = data.id).all()
		nav = [{
			'navtitle': i.name,
			'url': i.subcategory_url,
			'sort': i.sort,
		}for i in navdata]
		title = Category.query.filter_by(subcategory_url = fq).first()
		cahcedata = {'style': jsondata, 'nav': sorted(nav, key=lambda x:x['sort'], reverse=True), 'url':data.maincategory_url}
		cahcedata = json.dumps(cahcedata)
	return render_template('index/category-subdivision.html',data=cahcedata, title=title.name)


@category.route('/api/get/category/video/<id>', methods=["POST"])
def global_get_categoryvideo(id):
	data = get_category_videoclass(id)
	return jsonify(data)

#获取视频列表
@category.route('/api/get-videolist/category/<name>/sort/<sorttype>/page/<pagenaber>', methods=["POST"])
def global_category_videolistapi(name, sorttype, pagenaber):

	#print(name, sorttype, pagenaber)
	if name == None or '':
		return 'fuck1'
	if sorttype == None or '':
		return 'fuck2'
	if pagenaber == None or '':
		return 'fuck3'

	data = get_category_videolist(category_name=str(name), sort_type=sorttype, pagination=pagenaber)
	return jsonify(data)