import requests
import json


class Test_gettoken:
    def gettoken(self):
        url = "http://wlhy-apiserver.ntocc.test.chinawayltd.com/auth/applyToken"
        headers = {
            "content-type": "application/json;charset=UTF-8", }
        dates = {
            "userId": "6910",
            "password": "ac4e309509dcccaa6e7a8b94cbde3e73"
        }
        r = requests.post(url=url, headers=headers, data=json.dumps(dates))
        return r.text

    def test_tj(self):
        jsonData = json.loads(self.gettoken())
        token = jsonData["token"]
        print(token)
        return token
