import requests
import random
import hashlib
import time
import json
import string
import sys
import os

from Global import *

PATH = os.path.dirname(os.path.realpath(__file__))

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
        data = json.loads(req.text)
        if "成功" in data["data"]["msg"]:
            Cookie["stuid"] = str(data["data"]["cookie_info"]["account_id"])
            req = requests.get(url=cookieUrl2.format(Cookie["login_ticket"], Cookie["stuid"]))
            data = json.loads(req.text)
            Cookie["stoken"] = data["data"]["list"][0]["token"]
            print("登录成功！")
            return [1, Cookie]
        else:
            print("cookie已失效,请重新登录米游社抓取cookie")
            return [0, "cookie已失效,请重新登录米游社抓取cookie"]
    else:
        print("cookie中没有'login_ticket'字段,请重新登录米游社，重新抓取cookie!")
        return [0, "cookie中没有'login_ticket'字段,请重新登录米游社，重新抓取cookie!"]


def loadJson():
    try:
        with open(f"{PATH}/cookie.json", "r") as f:
            data = json.load(f)
            f.close()
            print("载入文件成功！")
            return data["Cookie"]
    except:
        c0 = mysCookie
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
    def __init__(self):
        self.Cookie = loadJson()
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
        print("正在签到......")
        for i in gameList:
            req = requests.post(url=signUrl.format(i["id"]), cookies=self.Cookie, headers=self.headers)
            data = json.loads(req.text)
            if "err" not in data["message"]:
                print(i["name"], data["message"])
                time.sleep(2)
            else:
                print("签到失败，你的cookie可能已过期，请重新设置cookie。")
                with open(f"{PATH}/cookie.json", "w") as f:
                    f.write('')
                    f.close()
                    sys.exit()

    def getList(self):
        List = []
        print("正在获取帖子列表......")
        for i in gameList:
            req = requests.get(url=listUrl.format(i["forumId"]), headers=self.headers)
            data = json.loads(req.text)
            for n in range(10):
                List.append([data["data"]["list"][n]["post"]["post_id"], data["data"]["list"][n]["post"]["subject"]])
            print("已获取{}个帖子".format(len(List)))
            time.sleep(2)
        return List

    def readArticle(self):
        print("正在看帖......")
        for i in range(3):
            req = requests.get(url=detailUrl.format(self.articleList[i][0]), cookies=self.Cookie, headers=self.headers)
            data = json.loads(req.text)
            if data["message"] == "OK":
                print("看帖：{} 成功".format(self.articleList[i][1]))
            time.sleep(2)

    def upVote(self):
        print("正在点赞......")
        for i in range(5):
            req = requests.post(url=voteUrl, cookies=self.Cookie, headers=self.headers,
                                json={"post_id": self.articleList[i][0], "is_cancel": False})
            data = json.loads(req.text)
            if data["message"] == "OK":
                print("点赞：{} 成功".format(self.articleList[i][1]))
            time.sleep(2)

    def share(self):
        print("正在分享......")
        req = requests.get(url=shareUrl.format(self.articleList[0][0]), cookies=self.Cookie, headers=self.headers)
        data = json.loads(req.text)
        if data["message"] == "OK":
            print("分享：{} 成功".format(self.articleList[0][1]))


if __name__ == '__main__':
    a = miYouBi()
    a.readArticle()
    a.upVote()
    a.share()
    print("任务全部完成")
