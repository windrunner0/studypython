import urllib.request
import re

url = "http://news.baidu.com/"
#伪装浏览器用户
headers = {'User-Agent':'User-Agent:Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:68.0) Gecko/20100101 Firefox/68.0'}
req = urllib.request.Request(url,headers=headers)

#执行请求获取响应信息
res = urllib.request.urlopen(req)

# 从响应对象中读取信息并解码
html = res.read().decode("utf-8")

print(len(html))
#print(html)
#使用正则解析出新闻标题信息
pat = '<a href="(.*?)" .*? target="_blank">(.*?)</a>'
dlist = re.findall(pat,html)

# 遍历输出结果
for v in dlist:
    str = re.search("http", v[0])
    print(str)
    if(str):
        print(v[1] + ":" + v[0])
