# -*- coding: utf-8 -*-
import requests
import random
import hashlib
import time
import json
import string
import sys
import os
import logging

from Global import *

PATH = os.path.dirname(os.path.realpath(__file__))



logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s %(levelname)s %(message)s',
    datefmt='%Y-%m-%dT%H:%M:%S')


log = logger = logging
def md5(text):
    """
    md5加密
    """
    md5 = hashlib.md5()
    md5.update(text.encode())
    return md5.hexdigest()


def randomStr(n):
    """
    生成指定位数随机字符串
    """
    return (''.join(random.sample(string.ascii_lowercase, n))).upper()


def DSGet():
    """
    生成DS
    """
    n = salt
    i = str(int(time.time()))
    r = randomStr(6)
    c = md5("salt=" + n + "&t=" + i + "&r=" + r)
    return "{},{},{}".format(i, r, c)


def getCookie(cookie):
    Cookie = {}
    if "login_ticket" in cookie:
        cookie = cookie.split(";")
        for i in cookie:
            if i.split("=")[0] == " login_ticket":
                Cookie["login_ticket"] = i.split("=")[1]
                break
        req = requests.get(url=cookieUrl.format(Cookie["login_ticket"]))
        data = json.loads(req.text.encode('utf-8'))
        if "成功" in data["data"]["msg"]:
            Cookie["stuid"] = str(data["data"]["cookie_info"]["account_id"])
            req = requests.get(url=cookieUrl2.format(Cookie["login_ticket"], Cookie["stuid"]))
            data = json.loads(req.text.encode('utf-8'))
            Cookie["stoken"] = data["data"]["list"][0]["token"]
            print("登录成功！")
            return [1, Cookie]
        else:
            print("cookie已失效,请重新登录米游社抓取cookie")
            return [0, "cookie已失效,请重新登录米游社抓取cookie"]
    else:
        print("cookie中没有'login_ticket'字段,请重新登录米游社，重新抓取cookie!")
        return [0, "cookie中没有'login_ticket'字段,请重新登录米游社，重新抓取cookie!"]


def loadJson(c0):
    try:
        with open(f"{PATH}/cookie.json", "r") as f:
            data = json.load(f)
            f.close()
            log.info("载入文件成功！")
            return data["Cookie"]
    except:
        c = getCookie(c0)
        if c[0]:
            data = {"Cookie0": c0, "Cookie": c[1]}
            with open(f"{PATH}/cookie.json", "w") as f:
                json.dump(data, f)
                f.close()
            return c[1]
        else:
            sys.exit()


class miYouBi:
    def __init__(self,):
        self.Cookie = loadJson(mysCookie)
        self.headers = {
            "DS": DSGet(),
            "x-rpc-client_type": client_type,
            "x-rpc-app_version": mysVersion,
            "x-rpc-sys_version": "6.0.1",
            "x-rpc-channel": "miyousheluodi",
            "x-rpc-device_id": randomStr(20) + randomStr(12),
            "x-rpc-device_name": randomStr(random.randint(1, 10)),
            "x-rpc-device_model": "Mi 10",
            "Referer": "https://app.mihoyo.com",
            "Host": "bbs-api.mihoyo.com",
            "User-Agent": "okhttp/4.8.0"
        }
        self.signIn()
        self.articleList = self.getList()

    def signIn(self):
        log.info("正在签到......")
        for i in gameList:
            req = requests.post(url=signUrl.format(i["id"]), cookies=self.Cookie, headers=self.headers)
            data = json.loads(req.text.encode('utf-8'))
            if "err" not in data["message"]:
                log.info(str(i["name"]+ data["message"]))
                time.sleep(2)
            else:
                log.info("签到失败，你的cookie可能已过期，请重新设置cookie。")
                with open(f"{PATH}/cookie.json", "w") as f:
                    f.write('')
                    f.close()
                    sys.exit()

    def getList(self):
        List = []
        log.info("正在获取帖子列表......")
        for i in gameList:
            req = requests.get(url=listUrl.format(i["forumId"]), headers=self.headers)
            data = json.loads(req.text.encode('utf-8'))
            for n in range(10):
                List.append([data["data"]["list"][n]["post"]["post_id"], data["data"]["list"][n]["post"]["subject"]])
            log.info("已获取{}个帖子".format(len(List)))
            time.sleep(2)
        return List

    def readArticle(self):
        log.info("正在看帖......")
        for i in range(3):
            req = requests.get(url=detailUrl.format(self.articleList[i][0]), cookies=self.Cookie, headers=self.headers)
            data = json.loads(req.text.encode('utf-8'))
            if data["message"] == "OK":
                log.info("看帖：{} 成功".format(self.articleList[i][1]))
            time.sleep(2)

    def upVote(self):
        log.info("正在点赞......")
        for i in range(5):
            req = requests.post(url=voteUrl, cookies=self.Cookie, headers=self.headers,
                                json={"post_id": self.articleList[i][0], "is_cancel": False})
            data = json.loads(req.text.encode('utf-8'))
            if data["message"] == "OK":
                
                log.info("点赞：{} 成功".format(self.articleList[i][1]))
            time.sleep(2)

    def share(self):
        log.info("正在分享......")
        req = requests.get(url=shareUrl.format(self.articleList[0][0]), cookies=self.Cookie, headers=self.headers)
        data = json.loads(req.text.encode('utf-8'))
        if data["message"] == "OK":
            log.info("分享：{} 成功".format(self.articleList[0][1]))


if __name__ == '__main__':
    a = miYouBi()
    a.readArticle()
    a.upVote()
    a.share()
    log.info("任务全部完成")
