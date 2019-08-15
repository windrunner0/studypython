#!/usr/bin/python3

import pymysql

# 打开数据库连接
db = pymysql.connect(host="localhost",user="root",password="root123",db="db_maven",charset="utf8")

# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()

# 使用 execute()  方法执行 SQL 查询
##cursor.execute("SELECT VERSION()")

cursor.execute("SELECT * FROM BOOK")

# 使用 fetchone() 方法获取单条数据.
##data = cursor.fetchone()
books = cursor.fetchall()
##print ("Database version : %s " % data)
for vo in books:
    print(vo)
##print("book info : ",book.bookid)
# 关闭数据库连接
db.close()