#!usr/bin/python3

n = 100
sum = 0
counter = 1
while counter <= n:
    sum = sum + counter
    counter += 1

print("从1到 %d 之间的和为： %d" % (n, sum))


print("死循环测试-----------------------------------------------")

var  = 1
while var == 1:
    num = int(input("输入一个数字： "))
    print("你输入的数字为： " , num)
    if num == 12:
        break;
    print("当前输入的数字为： ", num)

print("good bye !")



print("for in testing.........")

for i in range(10):
    print(i)

print("----------------------乘法口诀表-------------------------")

for i in range(1, 10):
    for j in range(1, i+1):
        print(str(i) + ' * ' + str(j) + ' = ' + str(i*j), end="  ")
    print()

print("---------------------------------逆向输出乘法口诀表-------------------------------")

for i in range(9, 0, -1):
    for j in range(i,0, -1):
        print(str(i) + ' * ' + str(j) + ' = '  + str(i * j), end = "   ")
    print()

print("")

