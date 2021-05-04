# -*- coding: utf-8 -*-
"""
在下面设置你的米游社Cookie
"""
mysCookie = ''
"""
以下内容不要改！！！
"""
mysVersion = "2.7.0"
salt = "fd3ykrh7o1j54g581upo1tvpam0dsgtf"  # 米游社2.7.0版本安卓客户端salt值
client_type = "2"  # 1:ios 2:android

"""
api
"""
cookieUrl = "https://webapi.account.mihoyo.com/Api/cookie_accountinfo_by_loginticket?login_ticket={}"
cookieUrl2 = "https://api-takumi.mihoyo.com/auth/api/getMultiTokenByLoginTicket?login_ticket={}&token_types=3&uid={}"
signUrl = "https://bbs-api.mihoyo.com/apihub/sapi/signIn?gids={}"  # post
listUrl = "https://bbs-api.mihoyo.com/post/api/getForumPostList?forum_id={}&is_good=false&is_hot=false&page_size=20&sort_type=1"
detailUrl = "https://bbs-api.mihoyo.com/post/api/getPostFull?post_id={}"
shareUrl = "https://bbs-api.mihoyo.com/apihub/api/getShareConf?entity_id={}&entity_type=1"
voteUrl = "https://bbs-api.mihoyo.com/apihub/sapi/upvotePost"  # post json 

"""
分区编号
"""
gameList = [
    {
        "id": "1",
        "forumId": "1",
        "name": "崩坏3",
        "url": "https://bbs.mihoyo.com/bh3/"
    },
    {
        "id": "2",
        "forumId": "26",
        "name": "原神",
        "url": "https://bbs.mihoyo.com/ys/"
    },
    {
        "id": "3",
        "forumId": "30",
        "name": "崩坏2",
        "url": "https://bbs.mihoyo.com/bh2/"
    },
    {
        "id": "4",
        "forumId": "37",
        "name": "未定事件簿",
        "url": "https://bbs.mihoyo.com/wd/"
    },
    {
        "id": "5",
        "forumId": "34",
        "name": "大别野",
        "url": "https://bbs.mihoyo.com/dby/"
    }
]
