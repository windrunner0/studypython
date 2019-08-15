# 导入模块
from bs4 import BeautifulSoup
import re
# 读取html文件信息（在真实代码中是爬取的网页信息）
f = open("./my.html",'r')
content = f.read()
f.close()

# 创建解析器
soup = BeautifulSoup(content,"lxml")


print(soup.select("ul li a")) #获取ul里面li下面的a元素节点

print(soup.select("#hid")) #获取id属性值为hid的元素节点

print(soup.select("li.shop a")) #获取class属性为shop的li元素里面所有的a元素节点

# 套用选择解析器
blist = soup.select("ul li")
for li in blist:
    a = li.select("a")[0] #获取每个li里面的a元素节点
    print(a)
    print(a['href']) #获取属性href的值
    # print(a.attrs['href']) #等价 同上 获取属性值
    print(a.get_text()) #等价 print(a.string) 获取元素节点的文本内容