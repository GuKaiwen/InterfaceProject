import requests
import json

class RunMethod:

    def post_main(self, url, data, header=None):
        res = None
        if header != None:
            res = requests.post(url=url, data=data, headers=header)
        else:
            res = requests.post(url=url, data=data)
        return res.json()

    def get_main(self, url, data=None, header=None):
        res = None
        if header != None:
            res = requests.get(url=url, data=data, headers=header)
        else:
            res = requests.get(url=url, data=data)
        return res.json()

    def run_main(self, method, url, data=None, header=None):
        res = None
        if method == 'POST':
            res = self.post_main(url=url, data=data, header=header)
        else:
            res = self.get_main(url=url, data=data, header=header)
        return json.dumps(res, ensure_ascii=False, sort_keys=True, indent=2)


if __name__ == '__main__':
    runmethod = RunMethod()
    print(runmethod.run_main('POST', 'http://www.imooc.com/api3/follow'))