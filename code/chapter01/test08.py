# !/usr/bin/python3

def hello():
    print("Hello Python");

hello();


# 计算面积函数
def area(width, height):
    return width * height

def print_welcome(name):
    print("Welcome", name)

print_welcome("Python")
w = 4
h = 5
print("width =", w, " height =", h, " area =", area(w, h))





def printme( str ):
   "打印任何传入的字符串"
   print (str);
   return;

#调用printme函数
printme("asdasdadas");


#可写函数说明
def printinfo( name, age = 35 ):
   "打印任何传入的字符串"
   print ("名字: ", name);
   print ("年龄: ", age);
   return;

#调用printinfo函数
printinfo( age=50, name="runoob" );
print ("------------------------")
printinfo( name="runoob" );









def printinfo( arg1, *vartuple ):
   "打印任何传入的参数"
   print ("输出: ")
   print (arg1)
   for var in vartuple:
      print (var)
   return;
# 调用printinfo 函数
printinfo( 10 );
printinfo( 70, 60, 50 );