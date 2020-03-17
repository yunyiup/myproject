import requests
from  bs4 import  BeautifulSoup

url="http://www.cntour.cn/"
response=requests.get(url)
# print(response.text)
soup=BeautifulSoup(response.text,'lxml')
data=soup.select("#slide1 > div.bd > ul:nth-child(2) > li > div > ul.tab > li:nth-child(2) > a")
print(data)

for item in data:
    result={
        'title':item.get_text(),
        'link':item.get('href')
    }
print(result)