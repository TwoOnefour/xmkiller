# @Time    : 2024/10/10 21:48
# @Author  : TwoOnefour
# @Email   : twoonefour@pursuecode.cn
# @File    : main.py

import requests
from main import *
from urllib3 import disable_warnings

disable_warnings()

def getcode():
    wx = WeChatApi(appid='wx014a3b75852905fe')

    code = json.loads(wx.login()["res"])["code"]
    wx.close()
    return code
class Checkout:
    disable_warnings()
    session = requests.Session()
    session.verify = False
    session.headers.update({"user-agent": "Mozilla/5.0 (Windows NT 10"})
    base_url = "https://d2.xksyun.com/"
    apis = {
        "list_services": "api4/personal_services/list_services",
        "load_service": "api4/personal_services/load_service",
        "create_service_record": "api4/personal_services/create_service_record",
        "list_service_records": "api4/personal_services/list_service_records"
    }
    wx_session_user_id = None
    code = getcode()



    def list_services(self):
        res = self.session.get(self.base_url + self.apis["list_services"] , params={
            "app": "weixin_api4_attend",
            "wx_session_user_id": "",
            "part": "我参与的",
            "page_num": "1",
            "keyword": "",
            "code": self.code,
        })
        if "wx_session_user_id" not in res.json():
            return
        self.wx_session_user_id = res.json()["wx_session_user_id"]
        # print(res.json())
        return res.json()['data']['services']

    def list_service_records(self, service_id):

        res = self.session.get(self.base_url + self.apis["list_service_records"], params={
            "app": "weixin_api4_attend",
            "wx_session_user_id": self.wx_session_user_id,
            "service_id": service_id,
            "part": "我参与的",
            "page_num": "1",
            "keyword": "",
            "code": self.code,
        })
        require_fields = {}
        for i in res.json()["data"]['fields']:
            if i['valid_presence']:
                require_fields[i['col_name']] = input(f'请输入需要签到的{i["title"]}:')
            else:
                require_fields[i['col_name']] = ""

        return require_fields

    def check_require_fields(self, service_id): # 'service_id': { "xxx": "xxx" } 用于对应service_id签到的数据
        if os.path.exists("require_fields.json"):
            rewrite_flag = False
            with open("require_fields.json", "r") as f:
                require_json_data = json.load(f)
                if service_id in require_json_data:
                    return require_json_data[service_id]
                else:
                    rewrite_flag = True
            if rewrite_flag:
                require_fields = self.list_service_records(service_id)
                with open("require_fields.json", "w") as f:
                    json.dump({service_id: require_fields}, f)
                return require_fields
        else:
            require_fields = self.list_service_records(service_id)
            with open("require_fields.json", "w") as f:
                json.dump({service_id: require_fields}, f)
            return require_fields

    def checkout(self, service_id, require_fields):
        res = self.session.post(self.base_url + self.apis["create_service_record"], params={
            "app": "weixin_api4_attend"
        }, json={
            "wx_session_user_id": self.wx_session_user_id,
            "service_record_id": None,
            "service_id": service_id,
            "service_record": require_fields,
            "delete_images_urls": [],
            "code": self.code
        })
        print(res.json()['msg'])

    def run(self):
        services = self.list_services()
        for i in services:
            print(f"找到签到项目{i['title']}")
            require_fields = self.check_require_fields(i['id'])
            if self.checkout(i['id'], require_fields) == '创建成功':
                print(f"{i['title']} 签到成功")





