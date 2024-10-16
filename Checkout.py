# @Time    : 2024/10/10 21:48
# @Author  : TwoOnefour
# @Email   : twoonefour@pursuecode.cn
# @File    : main.py

import requests
from main import *


def getcode():
    wx = WeChatApi(appid='wx014a3b75852905fe')
    code = json.loads(wx.login()["res"])["code"]
    wx.close()
    return code
def checkout():

    session = requests.Session()
    session.verify = False
    session.headers.update({"user-agent": "Mozilla/5.0 (Windows NT 10"})
    base_url = "https://d2.xksyun.com/"
    apis = {
        "list_services": "api4/personal_services/list_services",
        "load_service": "api4/personal_services/load_service",
        "create_service_record": "api4/personal_services/create_service_record",
        "list_service_records":"api4/personal_services/list_service_records"
    }
    code = getcode()
    res = session.get(base_url + apis["list_services"] , params={
        "app": "weixin_api4_attend",
        "wx_session_user_id": "",
        "part": "我参与的",
        "page_num": "1",
        "keyword": "",
        "code": code,
    })
    if "wx_session_user_id" not in res.json():
        return
    wx_session_user_id = res.json()["wx_session_user_id"]
    print(res.json())

    res = session.post(base_url + apis["create_service_record"], params={
        "app": "weixin_api4_attend"
    }, json={
        "wx_session_user_id": wx_session_user_id,
        "service_record_id":None,
        "service_id":"",
        "service_record":{
            "vbrhemcwhehg":"1",  # 名字,必填
            "lafkdagclrte":"17777777777"  # 电话
        },
        "delete_images_urls":[],
        "code":code
    })
    print(res.json())