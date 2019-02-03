import time
import tornado.ioloop
from submitdata import write_video_data, write_bangumi_data

time_30s = (1000*60)*0.5

time_60s = (1000*60)*1

time_2min = (1000*60)*2

tornado.ioloop.PeriodicCallback(write_video_data, time_30s).start()
tornado.ioloop.PeriodicCallback(write_bangumi_data, 10).start()