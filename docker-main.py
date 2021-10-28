import os
import Global
import schedule
import time

Global.mysCookie = os.environ.get('MYS_COOKIE', Global.mysCookie)
if not Global.mysCookie:
    raise Exception("cookie is empty")

# 每日启动时间
SCHEDULE_AT = os.environ.get("SCHEDULE_AT", "01:00")


def main():
    from myb import miYouBi
    a = miYouBi()
    a.readArticle()
    a.upVote()
    a.share()
    print("任务全部完成")


if __name__ == '__main__':
    schedule.every(1).day.at(SCHEDULE_AT).do(main)
    main()
    while True:
        schedule.run_pending()
        time.sleep(1)
