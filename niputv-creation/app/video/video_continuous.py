import datetime
import requests
from app.video.transcoding import if_transcoding_condition, transcoding_distribution
from app.elastic.elastic_video_operating import write_videomain
from app.Database.db_video import Videofile
from app.Database.db_user import video_quantity_plus

#视频进入持续化处理
def continuous_video_transcoding(key):

    #获取视频参数
    videoinfo = get_cachevideo_info(key)
    videotime = videoinfo['video_duration'] #视频长度
    videowidth = videoinfo['video_width'] #视频宽度
    videoheight = videoinfo['video_height'] #视频高度

    #判断视频清晰度条件 符合条件的清晰度会返回true 不符合返回False
    sharpness = if_transcoding_condition(width=videowidth, height=videoheight)
    video4k = sharpness['4k']
    video2k = sharpness['2k']
    video360p = sharpness['360p']
    video480p = sharpness['480p']
    video720p = sharpness['720p']
    video1080p = sharpness['1080p']

    #把视频提交到转码发起机制{v360 = true if v360 = true 执行 video_transcoding('文件','清晰度')}
    transcoding_distribution(key=key, v360=video360p, v480=video480p, v720=video720p, v1080=video1080p, v2k=video2k, v4k=video4k)

    return {'key':key ,'videotime':videotime, 'videowidth':videowidth, 'videoheight': videoheight, 'v360':sharpness['360p'], 'v480':sharpness['480p'], 'v720':sharpness['720p'], 'v1080':sharpness['1080p'], 'v2k':sharpness['2k'], 'v4k':sharpness['4k']}

#获取视频高宽信息
def get_cachevideo_info(key):
	videoinfo = requests.get('http://pckk76m2j.bkt.clouddn.com/'+ key +'?avinfo')
	videoinfo = videoinfo.json()
	if(videoinfo):
		video_width = videoinfo['streams'][0]['width']
		video_height = videoinfo['streams'][0]['height']
		try:
			video_time = videoinfo['streams'][0]['duration']
		except:
			video_time = videoinfo['format']['duration']

		#格式化取出视频时长
		#time = str(datetime.timedelta(seconds=int(float(video_time))))

		#取整数秒
		time = int(float(video_time))

		videoinfo = {
			'video_width': video_width,
			'video_height': video_height,
			'video_duration': time,
		}
		return videoinfo

def write_videoinfo(data, videoid, k4):

    print('写入视频金数据库')
    print(videoid)
    print(data)

    #更新视频时长信息 (视频id 视频长度 4K条件)
    write_videomain(videoid=videoid,video_duration=data['videotime'], grade_4k=k4)

    #储存进数据库
    Videofile(videoid=videoid, filekey=data['key'], clear360=data['v360'], clear480=data['v480'], clear720=data['v720'], clear1080=data['v1080'], clear2k=data['v2k'], clear4k = data['v4k'])

    #上传视频数量+1
    video_quantity_plus()