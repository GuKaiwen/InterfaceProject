import json

class OperationJson:

    def __init__(self, filename=None):
        if filename !=None:
            self.filename = filename
        else:
            self.filename = '../dataconfig/login.json'
        self.data = self.read_data()

    def read_data(self):
        with open(self.filename, 'r') as fp:
            data = json.load(fp)
            return data

    def get_data(self, key):
        return self.data[key]

    def write_data(self, data):
        with open('../dataconfig/cookie.json', 'w') as fp:
            fp.write(json.dumps(data))

if __name__ == '__main__':
    opera_json = OperationJson()
    print(opera_json.read_data())
    print(opera_json.get_data('username1'))


