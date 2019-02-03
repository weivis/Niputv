from app.cloud import video_transcoding

#判断视频可转码清晰度(传入{v360 = true if v360 = true 执行 video_transcoding('文件','清晰度')})
def transcoding_distribution(key, v360, v480, v720, v1080, v2k, v4k):
    if v360 == True:
        video_transcoding(key, '360p')

    if v480 == True:
        video_transcoding(key, '480p')

    if v720 == True:
        video_transcoding(key, '720p')

    if v1080 == True:
        video_transcoding(key, '1080p')

    if v2k == True:
        video_transcoding(key, '2k')

    if v4k == True:
        video_transcoding(key, '4k')

#判断视频可转换清晰度
def if_transcoding_condition(width, height):
	video_360p = False
	video_480p = False
	video_720p = False
	video_1080p = False
	video_2k = False
	video_4k = False

	#360P 640X360 -10
	'''
	if height > 350:
		if width > 630:
	'''
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

	#2K 2560x1440 -10
	if height > 1430:
		if width > 2550:
			video_2k = True

	#2K 3840x2160 -10
	if height > 2150:
		if width > 3830:
			video_4k = True

	pxlist = {
		'360p': video_360p,
		'480p': video_480p,
		'720p': video_720p,
		'1080p': video_1080p,
		'2k': video_2k,
		'4k': video_4k,
	}
	return pxlist
