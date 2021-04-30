"""
在下面设置你的米游社Cookie
"""
mysCookie = '_ga_E36KSL9TFE=GS1.1.1611330164.2.1.1611330369.0; _ga_KJ6J9V9VZQ=GS1.1.1612097208.2.1.1612097227.0; CNZZDATA1275023096=569536731-1600871848-https%253A%252F%252Fys.mihoyo.com%252F%7C1613751480; _ga_FLGX56JEBS=GS1.1.1614340834.4.1.1614343143.0; mi18nLang=zh-cn; _ga=GA1.2.2019832523.1600876290; _ga_ELSF9S5LND=GS1.1.1619582652.1.1.1619582703.0; _MHYUUID=7dfcee7d-b822-4b29-bd49-06f5cb85c4a8; login_uid=161842485; login_ticket=BQFHpXauLLUK3GEPqedWBHGTVQBDxdoxtxBvVJ1e; account_id=161842485; cookie_token=8HTySB3PTSqYbRyTzUFU9tGeAKdkOucAXdt4WtKJ; ltoken=M4VvfQV2cHfhj7qkVTgG4HXH94tuiaANBEQO3E31; ltuid=161842485'

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
cookieUrl2 = "https://bbs-api.mihoyo.com/auth/api/getMultiTokenByLoginTicket?login_ticket={}&token_types=3&uid={}"
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