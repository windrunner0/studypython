#!usr/bin/python3

def printinfo(name, age = 35):
    print("名字：" , name)
    print("年龄：", age)
    return;

printinfo("郑鹏", 26);
print()
printinfo(name="二狗");
print()
printinfo(age=900,name="涛涛");


def info(arg1, *vartuple):
    print("输出：")
    print(arg1);
    for var in vartuple:
        print(var);
    return;

info(10);
info(70, 60, 50)

print("匿名函数测试--------------------------")
sum = lambda arg1 , arg2 : arg1 + arg2;
print(sum(10, 20))
print(sum(20, 20))

##print(random())

##print(pi)






