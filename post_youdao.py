import requests


url="http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule"
form_data={
    'i': '我和你都是',
    'from':' AUTO',
    'to': 'AUTO',
    'smartresult': 'dict',
    'client': 'fanyideskweb',
    'salt': '15846843266453',
    'sign': 'dc2335b4f1adfd8e66e907cfc07762b5',
    'ts': '1584684326645',
    'bv': '3a019e7d0dda4bcd253903675f2209a5',
    'doctype': 'json',
    'version': '2.1',
    'keyfrom': 'fanyi.web',
    'action':'FY_BY_CLICKBUTTION',
}
response=requests.post(url,form_data)
print(response.text)
