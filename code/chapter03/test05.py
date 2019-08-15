from bs4 import BeautifulSoup
import re
# 读取html文件信息（在真实代码中是爬取的网页信息）
f = open("./my.html",'r',encoding="utf-8")
content = f.read()
f.close()

# 创建解析器
soup = BeautifulSoup(content,"lxml")

# 通过name指定li值，获取所有li元素节点,返回列表
lilist = soup.find_all(name="li")
print(lilist)
# 通过attrs指定属性来获取所有元素节点
lilist = soup.find_all(attrs={"class":"aa"})
print(lilist)
lilist = soup.find_all(class_="aa") #同上(class属性中包含就可以了)
print(lilist)
lilist = soup.find_all(class_="shop") #class属性值中包含shop的所有节点
print(lilist)
lilist = soup.find_all(id="hid") #<h3 id="hid">我的常用链接</h3>
print(lilist)
# 通过文本内容获取
lilist = soup.find_all(text='百度') # 百度
print(lilist)
lilist = soup.find_all(text=re.compile('新')) # 张翠山 张无忌
print(lilist)
for i in lilist:
    print(i)


# 获取一个li元素节点
lilist = soup.find(name="li")
print(lilist)
# 通过attrs指定属性来获取一个元素节点
lilist = soup.find(attrs={"class":"aa"})
print(lilist)