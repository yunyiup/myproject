import requests
import unittest

# url="http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule"
# content="我和你"

# 用类解决全局变量的问题  面向对象的开发
class Youdao():
    # 全局变量变成实体变量
    def __init__(self,content):
        self.content=content
        self.url="http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule"
        self.ts=self.get_ts()
        self.salt=self.get_salt()
        self.sign=self.get_sign()
    def get_salt(self):
        # 随机产生0到10的整数
        import random
        s=str(random.randint(0,10))
        # salt=get_ts()+s
        salt=self.ts+s
        # print("salt=",salt)
        return salt
    def get_md5(self,value):
        import hashlib
        m=hashlib.md5()
        m.update(value.encode("utf-8"))
        return m.hexdigest()
    # def  get_content(self):
    #     return content
    def get_sign(self):
        # i=get_salt()
        # e=get_content()
        i=self.salt
        e=self.content
        s="fanyideskweb" + e + i + "Nw(nmmbP%A-r6U3EUn]Aj"
        # print("s=",s)
        # print("sian=", self.get_md5(s))
        return self.get_md5(s)
    def get_ts(self):
        # 时间戳
        import time
        t = time.time()
        ts = str(int(round(t * 1000)))
        # print("ts=",ts)
        return ts

    # 全局变量抽成新函数
    def yield_form_data(self):
        # ''里不能有空格
        form_data={
            'i': self.content,
            'from':' AUTO',
            'to': 'AUTO',
            'smartresult': 'dict',
            'client': 'fanyideskweb',
            # 'salt': get_salt(),
            # 'sign': get_sign(),
            # 'ts': get_ts(),
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
        # ''里不能有空格
        headers={
            'Cookie': 'OUTFOX_SEARCH_USER_ID=1278658854@10.108.160.100',
            'Referer':'http://fanyi.youdao.com/',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36',
        }
        return headers

    def fanyi(self):

        response = requests.post(self.url, data=self.yield_form_data(), headers=self.get_headers())
        import json
        content=json.loads(response.text)
        # return response.text
        # print(content)
        # 从结果字典中取出需要的内容
        return content['translateResult'][0][0]['tgt']

if __name__ == '__main__':
  # print(form_data)
  # print(get_headers())
  # response = requests.post(url, data=form_data(), headers=get_headers())
  # print(response.text)
  while(True):
      i=input("please input:")
      youdao=Youdao(i)
      print("result:",youdao.fanyi())

