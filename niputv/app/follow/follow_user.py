from app import Flask, db, cache
from app.Database.db_features import Follow_author
from app.account import Account
from flask_login import current_user

def follow_orm(be_follow_userid):
    if be_follow_userid == current_user.id:
        return "{'code':'error follow user no is me'}"
    #查询传递进来的被订阅用户是否存在 
    account = Account.query.filter_by(id = be_follow_userid).first()
    if (account):

        #查询是否已经关注过 已关注过则删除 未关注则添加
        followdata = Follow_author.query.filter_by(user_id=current_user.id ,follow_user=be_follow_userid).first()
        if (followdata):
            #删除该订阅记录
            db.session.delete(followdata)

            newfan_statistics = Account.fan_statistics - 1
            db.session.query(Account).filter(Account.id == current_user.id).update({Account.fan_statistics:newfan_statistics})

            db.session.commit()
            return 'del'

        else:
            #添加记录
            data = Follow_author(follow_user = be_follow_userid)
            db.session.add(data) 

            newfan_statistics = Account.fan_statistics + 1
            db.session.query(Account).filter(Account.id == current_user.id).update({Account.fan_statistics:newfan_statistics})

            db.session.commit()
            return 'add'
    else:
        return 'error'

def follow_gettype(be_follow_userid):
    followdata = Follow_author.query.filter_by(user_id=current_user.id ,follow_user=be_follow_userid).first()
    if (followdata):
        return True
    else:
        return False