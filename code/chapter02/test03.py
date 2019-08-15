#!/usr/bin/python3
print("start.....")
try:
    x = int(input("Please enter a number: "))
    print("number:",x)
    print(100/x)
    print("ok....")
except ValueError:
    print("非纯数字错误！")
except ZeroDivisionError:
    print("不可以为零错误！")
except:
    print("可选的未知错误！")
print("end.....")