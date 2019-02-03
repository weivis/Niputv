__author__ = 'Ran'
from app import Flask, cache, login_manager
from ..user import user
from app.account import Account
from flask import render_template, request, session, redirect
from app.Database.db_features import Subscription_bangumi
from app.elastic.elastic_bangumi import query_bangumi_data
from flask_login import current_user
import json

#番剧
@user.route('/bangumi')
def bangumi():
    return render_template('user/bangumi.html')

#首页
@user.route('/bangumilist/<page>', methods=["POST"])
def bangumilist(page):
    if page == 0:
        page == 1
    data = Subscription_bangumi.query.filter_by(sub_user = current_user.id).order_by("sub_time").limit(int(page*10)).offset(0)
    list = [{
        'bangumi_id': i.sub_bangumi,
        'bangumi_cover': query_bangumi_data(i.sub_bangumi)['_source']['cover'],
        'bangumi_name': query_bangumi_data(i.sub_bangumi)['_source']['name'],
        'bangumi_introduction': query_bangumi_data(i.sub_bangumi)['_source']['introduction'][0:60],
        'subtime': i.sub_time,
    }for i in data]
    return json.dumps(list)

#订阅
@user.route('/subscription')
def subscription():
    return render_template('user/subscription.html')

#历史
@user.route('/history')
def history():
    return render_template('user/history.html')