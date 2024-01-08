import requests
from util.operation_json import OperationJson

# url = 'http://www.imooc.com/passport/user/login'
# data = {
#         "username": "18721268250",
#         "password": "xxx",
#         "verify": "",
#         "referer": "https://www.imooc.com"
# }
# response = requests.post(url=url, data=data).json()
# response_url = response['data']['url'][0]
# request_url = response_url+'&callback=jQuery1113023368003966082806_1703684544517&_=1703684544519'
#
# cookie = requests.get(request_url).cookies
# cookie = requests.utils.dict_from_cookiejar(cookie)
# print(cookie)
#
# url1 = 'http://www.imooc.com/common/activity-grantcoupon?callback=jQuery224038699237246162976_1703685309670&_=1703685309671'
#
# res = requests.get(url1)
# print(res.text)

class OperationHeader:

    def __init__(self, res):
        self.res =res
        self.opera_json = OperationJson()

    def write_cookie(self):
        response_url = self.res['data']['url'][0]
        request_url = response_url + '&callback=jQuery1113023368003966082806_1703684544517&_=1703684544519'
        cookie = requests.get(request_url).cookies
        cookie = requests.utils.dict_from_cookiejar(cookie)
        self.opera_json.write_data(cookie)


if __name__ == '__main__':
    url = 'http://www.imooc.com/passport/user/login'
    data = {
        "username": "18721268250",
        "password": "xxx",
        "verify": "",
        "referer": "https://www.imooc.com"
    }
    res = requests.post(url=url, data=data).json()
    opera_header = OperationHeader(res)
    opera_header.write_cookie()