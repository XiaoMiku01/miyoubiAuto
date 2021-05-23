import myb
import time
import random

while True:
    a=myb.miYouBi()
    a.readArticle()
    a.upVote()
    a.share()
    now_time = int(time.time())
    nextday_time = now_time - now_time % 86400 + time.timezone + 86400
    sleep_time = nextday_time - now_time + random.randrange(3600)   
    #这里使用随机数来防止每天固定时间进行签到被识别，最长延迟1小时 
    time.sleep(sleep_time)
