from functools import wraps
from flask import session, redirect, url_for
from flask_login import current_user
import json

# 登录限制的装饰器
def auth_is_login(func):
 
	@wraps(func)
	def wrapper(*args,**kwargs):
		if current_user.is_authenticated:
			return func(*args,**kwargs)
		else:
			return json.dumps({"code":"10086"})
	return wrapper