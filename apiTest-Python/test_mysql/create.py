# -*- coding: UTF-8 -*-

import MySQLdb

# 打开数据库连接
db=MySQLdb.connect('localhost','root','123456','book')

# 使用cursor()方法获取操作游标
cursor = db.cursor()

# 创建数据表SQL语句
sql = """CREATE TABLE EMPLOYEE (
         FIRST_NAME  CHAR(20) NOT NULL,
         LAST_NAME  CHAR(20),
         AGE INT,  
         SEX CHAR(1),
         INCOME FLOAT )"""

cursor.execute(sql)

# 关闭数据库连接
db.close()