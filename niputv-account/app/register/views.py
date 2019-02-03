__registeror__ = 'Ran'
from app import Flask, cache, login_manager, db
from ..register import register
from flask import render_template, request, redirect, url_for
from flask_bcrypt import generate_password_hash
from app.Database.account import Account
import json
import re
from flask_login import login_user, login_required, logout_user, current_user

#注册
@register.route('/', methods=["GET","POST"])
def register_main():
    if current_user.is_authenticated:
        return redirect('http://www.niputv.com/')

    if request.method == 'POST':
        jsondata = request.json
        
        if jsondata['username'] == '':
            return json.dumps({'code':'false', 'text':'用户名不能为空'})

        if jsondata['useremail'] == '':
            return json.dumps({'code':'false', 'text':'邮箱不能为空'})

        if jsondata['phone'] == '':
            return json.dumps({'code':'false', 'text':'手机不能为空'})

        if jsondata['password'] == '':
            return json.dumps({'code':'false', 'text':'密码不能为空'})

        if Account.query.filter_by(username = jsondata['username']).first():
            return json.dumps({'code':'false', 'text':'用户名已存在'})

        if Account.query.filter_by(phone = jsondata['phone']).first():
            return json.dumps({'code':'false', 'text':'该手机已经注册过'})

        if Account.query.filter_by(user_email = jsondata['useremail']).first():
            return json.dumps({'code':'false', 'text':'该邮箱以注册过'})
            
        else:
            print(jsondata['password'])
            generate_newuserdata = Account(username=jsondata['username'], phone = jsondata['phone'], password = str(jsondata['password']), user_email = jsondata['useremail'])
            db.session.add(generate_newuserdata)
            db.session.commit()
            return json.dumps({'code':'True', 'text':'注册成功'})

    else:
        return render_template('main/register.html')