from app import Flask, db, cache
from app.Database.db_features import Follow_author
from flask_login import current_user
from app.Database.db_features import Subscription_bangumi
from app.elastic.elastic_bangumi import adddel_bangumi_sub_statistics

def delbangumisub(sub):
    adddel_bangumi_sub_statistics(tp='del', id=sub.sub_bangumi)
    db.session.delete(sub)
    db.session.commit()

def addbangumisub(id):
    adddel_bangumi_sub_statistics(tp='add', id=id)
    data = Subscription_bangumi(sub_bangumi=id)
    db.session.add(data)
    db.session.commit()