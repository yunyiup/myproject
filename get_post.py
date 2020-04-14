import requests
import unittest
import random
import hashlib
import time
import json

class Youdao():
    def __init__(self,content):
        self.content=content
        self.url="http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule"
        self.ts=self.get_ts()
        self.salt=self.get_salt()
        self.sign=self.get_sign()
    def get_salt(self):
        return self.ts + str(random.randint(0, 10))
    def get_md5(self,value):
        m=hashlib.md5()
        m.update(value.encode("utf-8"))
        return m.hexdigest()
    def get_sign(self):
        s = "fanyideskweb" + self.content + self.salt + "Nw(nmmbP%A-r6U3EUn]Aj"
        return self.get_md5(s)
    def get_ts(self):
        return str(int(round(time.time() * 1000)))
    def yield_form_data(self):
        form_data={
            'i': self.content,
            'from':' AUTO',
            'to': 'AUTO',
            'smartresult': 'dict',
            'client': 'fanyideskweb',
            'salt': self.salt,
            'sign': self.sign,
            'ts': self.ts,
            'bv': '3a019e7d0dda4bcd253903675f2209a5',
            'doctype': 'json',
            'version': '2.1',
            'keyfrom': 'fanyi.web',
            'action':'FY_BY_REALTlME',
        }
        return form_data
    def get_headers(self):
        headers={
            'Cookie': 'OUTFOX_SEARCH_USER_ID=1278658854@10.108.160.100',
            'Referer':'http://fanyi.youdao.com/',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36',
        }
        return headers
    def fanyi(self):
        response = requests.post(self.url, data=self.yield_form_data(), headers=self.get_headers())
        content=json.loads(response.text)
        return content['translateResult'][0][0]['tgt']
if __name__ == '__main__':
  while(True):
      i=input("please input:")
      youdao=Youdao(i)
      print("result:",youdao.fanyi())