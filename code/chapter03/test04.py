# 导入模块
from bs4 import BeautifulSoup

# 读取html文件信息（在真实代码中是爬取的网页信息）
f = open("./my.html",'r',encoding="utf-8")
content = f.read()
f.close()

# 创建解析器
soup = BeautifulSoup(content,"lxml")

# 输出网页内容：注：此内容已被缩进格式化（自动更正格式），其实这个是在上一步实例化时就已完成
#print(soup.prettify())

#输出网页中title标签中的内容
print(soup.title.string)
print(soup.title) #<title>我的网页</title>
print(type(soup.title)) #<class 'bs4.element.Tag'>
print(soup.head) #获取整个head元素，及内部元素
print(soup.li) #获取第一个li元素（后面其他li不会获取）

print("-------------------------------------------------------")
print(soup.a) #获取第一个a元素标签： <a class="bb" href="http://www.baidu.com">百度</a>
print(soup.a.name)    #获取标签名： a
print(soup.a.attrs)    #获取所有属性：{'class': ['bb'], 'href': 'http://www.baidu.com'}
print(soup.a.attrs['href']) #获取其中一个属性：http://www.baidu.com
print(soup.a.string) # 获取元素标签中间的文本内容：百度



print(soup.li.a) #获取网页中第一个li中的第一个a元素节点



print(type(soup.body.h3))  ##获取body中的第一个h3元素的类型：<class 'bs4.element.Tag'>
print(soup.body.h3.string)  #获取body中的第一个h3中的文本内容： 我的常用链接

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

# 子或子孙节点
# 以下获取的节点列表都可以使用for...in遍历
print(soup.ul.contents) #获取ul下面的所有直接子节点，返回列表
print(soup.ul.children) #获取ul下面的所有直接子节点，返回一个：<list_iterator object at 0x110346a20>

print(soup.ul.descendants) # 获取ul下的所有子孙节点。
for v in soup.ul.descendants:
    print("a:",v)

# 父祖节点
print(soup.a.parent.name) #通过parent属性获取a的父节点 li
# print(list(soup.a.parents)) # 获取所有祖先节点

#兄弟节点
print(soup.li.next_siblings)    #获取指定li节点的所有后面的兄弟节点
print(soup.li.previous_siblings)#获取指定li节点的所有前面的兄弟节点
#for v in soup.li.next_siblings:
#    print(v)

# 获取信息

print(soup.a.string) #获取a节点中的文本
print(soup.a.attrs['href']) # 或a节点的href属性值




