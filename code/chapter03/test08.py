# 读取my.html的文件内容，并使用pyquery来查找节点
from pyquery import PyQuery as pq

#doc = pq(filename='index.html',encoding="utf-8")


with open("./my.html","r",encoding="utf-8")as f:
    content = f.read()
doc = pq(content)



#print(doc('title')) #通过html标签名获取元素节点
#print(doc('#hid'))  #获取id属性值为hid的元素节点
#print(doc('.bb'))  #获取class属性值为bb的元素节点
print(doc('title,h3')) #选择符组的使用

print(doc("ul li.shop a")) #关联选择符的使用

print(doc("a")) #获取所有a
print(doc("a:first")) #获取第一个a
print(doc("a:last")) #获取最后一个a
print(doc("a:lt(2)")) #获取前连个a
print(doc("a:eq(2)")) #获取索引位置2的a（第三个）

print(doc('a[href="http://www.sina.com"]')) #获取指定属性值的节点

print("="*60)
# 节点的二次筛选：

lilist = doc("ul li") #获取ul中所有的li
print(type(lilist)) #<class 'pyquery.pyquery.PyQuery'>
print(lilist.find("a.bb")) #在结果的基础上再次查找
print(lilist.children("a.bb")) #在结果的基础上再次查找

print(doc("a.bb").parent()) #获取指定元素的直接父节点
#print(doc("a.bb").parents()) #获取指定元素的所有父节点
print(doc("a.bb").parent().siblings()) #获取兄弟节点

print("="*60)
# 遍历：

alist = doc("a")
for a in alist.items():
    print(a.attr.href)
    #print(a.attr('href')) #同上
    print(a.text())  #获取内容
    print(a.html())

