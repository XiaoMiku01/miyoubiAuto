# -*- coding: utf-8 -*-
import json
import random
from myb import miYouBi, getCookie, DSGet, randomStr
from Global import *
import sys


class mybCloud(miYouBi):
    def __init__(self, c0):
        self.Cookie = eval(c0)
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



def main_handler(event, context):
    data = json.loads(context['environment'])
    c0 = data['mysCookie']
    a = mybCloud(c0)
    a.readArticle()
    a.upVote()
    a.share()
    return '执行成功'


if __name__ == '__main__':
    if len(sys.argv) == 2:
        req = getCookie(sys.argv[1])
        if req[0] == 1:
            print(req[1])
        else:
            sys.exit()
    else:
        print('你输入的有误,请务必用双引号包裹cookie')
