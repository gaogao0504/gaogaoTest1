import requests
import json

from pythoncode.tj import Sm2Utils
from pythoncode.tj.constant import Gansu


class Test_tokenutils:

    def test_get(self):
        headers = {'Content-Type': 'application/json'}
        data = {"userId": Gansu.USER_ID, "password": Gansu.PASSWORD}
        res = requests.post(Gansu.URL + "/auth/applyToken", headers=headers, data=json.dumps(data))
        print(res.text)
        return res.text

    def test_tj(self):
        jsonData = json.loads(self.test_get())
        token = jsonData["token"]
        print(token)

    def test_sm(self):
        msg = Sm2Utils.encrypt("我是中国人")
        print(msg)


