import json

#案例一、这是一段过程化代码编写：
str= '[{"name":"zhangsan","age":22},{"name":"lisi","age":19},{"name":"wangwu","age":24}]'
data = json.loads(str) #解码JSON数据
# 过滤出年龄大于20岁以上的信息，并输出
for item in data:
    if item['age']>20:
        #输出数据
        print('-' * 20)
        print(item['name'],":",item['age'])
