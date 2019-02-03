import tornado.web
from video import write_video_playrecording, video_viewsdataget_rs, video_viewsdataget_count
from bangumi import write_bangumi_playrecording, bangumi_viewsdataget_bangumi_line, bangumicount_viewsdataget_count
import json

#跨域设置
class BaseHandler(tornado.web.RequestHandler):

    def set_default_headers(self):
        self.set_header("Access-Control-Allow-Origin", "*")  # 这个地方可以写域名
        self.set_header("Access-Control-Allow-Headers", "x-requested-with")
        self.set_header('Access-Control-Allow-Methods', 'POST, GET, OPTIONS')

    def post(self):
        self.write('some post')

    def get(self):
        self.write('some get')

    def options(self):
        # no body
        self.set_status(204)
        self.finish()

#视频播放量统计
class video_countAPI(tornado.web.RequestHandler):

    def get(self, video_id, ip):

        # videoid转为字符串
        video_id = str(video_id)

        # 判断视频id是否为空
        if video_id == '' or video_id == None:
            return self.set_status(404)

        # 如果存在传入视频id则正常
        else:
            # 判断是否存在优先级ip地址 不存在则使用系统获取ip
            if ip == '' or ip == None:
                ip = self.request.remote_ip
            else:
                ip = ip

            #write_playrecording()写入播放记录
            write_video_playrecording(video_id=video_id, ip=ip)

        #self.write("当前访问ip:" + ip + " 视频id:" + video_id)

#番剧播放量统计
class bangumi_countAPI(tornado.web.RequestHandler):

    def get(self, video_id, ip):

        # videoid转为字符串
        video_id = str(video_id)

        # 判断视频id是否为空 空属于非法请求
        if video_id == '' or video_id == None:
            return self.set_status(404)

        else:

            # 判断是否存在ip 不存在属于不合法请求
            if ip == '' or ip == None:
                return self.set_status(404)

            else:
                #write_bangumi_playrecording()写入番剧播放记录
                write_bangumi_playrecording(video_id=video_id, ip=ip)

#视频播放量统计
class datawc(tornado.web.RequestHandler):

    def get(self):

        data1 = bangumi_viewsdataget_bangumi_line()
        data2 = video_viewsdataget_rs()

        self.write(json.dumps({"video":json.dumps(data2),"bangumi":json.dumps(data1)}))
        #self.write("当前访问ip:" + ip + " 视频id:" + video_id)

#视频播放量统计
class getcount(tornado.web.RequestHandler):

    def get(self):

        data1 = bangumicount_viewsdataget_count()
        data2 = video_viewsdataget_count()

        self.write(json.dumps({"video":json.dumps(data2),"bangumi":json.dumps(data1)}))
        #self.write("当前访问ip:" + ip + " 视频id:" + video_id)