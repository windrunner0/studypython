# URL初始化
from pyquery import PyQuery as pq
doc = pq(url="http://www.baidu.com",encoding="utf-8")
print(doc('title'))

# 文件初始化
from pyquery import PyQuery as pq
doc = pq(filename='./my.html',encoding="utf-8")
print(doc('title'))


# 推荐使用requests爬取信息
from pyquery import PyQuery as pq
import requests
res = requests.get("http://www.baidu.com")
res.encoding = "utf-8" #因为原编码为ISO-8859-1
#print(res.text)
doc = pq(res.text)
print(doc("title"))