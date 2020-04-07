import requests


url="http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule"


def get_salt():
    # 随机产生0到10的整数
    import random
    s=str(random.randint(0,10))
    salt=get_ts()+s
    print("salt=",salt)
    return salt


def get_sign():
    return 'dc2335b4f1adfd8e66e907cfc07762b5'


def get_ts():
    # 时间戳
    import time
    t = time.time()
    ts = str(int(round(t * 1000)))
    print("ts=",ts)
    return ts


form_data={
    'i': '我和你都是',
    'from':' AUTO',
    'to': 'AUTO',
    'smartresult': 'dict',
    'client': 'fanyideskweb',
    'salt': get_salt(),
    'sign': get_sign(),
    'ts': get_ts(),
    'bv': '3a019e7d0dda4bcd253903675f2209a5',
    'doctype': 'json',
    'version': '2.1',
    'keyfrom': 'fanyi.web',
    'action':'FY_BY_CLICKBUTTION',
}
response=requests.post(url,form_data)
print(response.text)
