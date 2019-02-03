from app import db
from app.cloud import video_transcoding
from app.Database.db_videofile import Bangumi_video, uploads_bangumi_videoclear
from flask_login import current_user
import requests

def continuous_video_transcoding(key, bangumi_id, cover, videoname, videosort):

        videoinfo = get_cachevideo_info(key)
        videotime = videoinfo['video_duration']
        videowidth = videoinfo['video_width']
        videoheight = videoinfo['video_height']

		#获取视频清晰度
        sharpness = if_transcoding_condition(width=videowidth, height=videoheight)
        video360p = sharpness['360p']
        video480p = sharpness['480p']
        video720p = sharpness['720p']
        video1080p = sharpness['1080p']
        transcoding_distribution(key=key, v360=video360p, v480=video480p, v720=video720p, v1080=video1080p)
        dbop = Bangumi_video(filekey=key, cover=cover, bangumi_id=bangumi_id, video_name=videoname, video_sort=videosort, clear360=video360p, clear480=video480p, clear720=video720p, clear1080=video1080p)
        db.session.add(dbop)
        db.session.commit()

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


def if_transcoding_condition(width, height):
	video_360p = False
	video_480p = False
	video_720p = False
	video_1080p = False

	#360P 640X360 -10
	if height > 350:
		if width > 640:
			video_360p = True

	#480P 852x480 -10
	if height > 470:
		if width > 842:
			video_480p = True

	#720P 1280X720 -10
	if height > 710:
		if width > 1270:
			video_720p = True

	#1080P 1920X1080 -10
	if height > 1070:
		if width > 1910:
			video_1080p = True

	pxlist = {
		'360p': video_360p,
		'480p': video_480p,
		'720p': video_720p,
		'1080p': video_1080p,
	}
	return pxlist

def transcoding_distribution(key, v360, v480, v720, v1080):
    if v360 == True:
        video_transcoding(key, '360p')

    if v480 == True:
        video_transcoding(key, '480p')

    if v720 == True:
        video_transcoding(key, '720p')

    if v1080 == True:
        video_transcoding(key, '1080p')