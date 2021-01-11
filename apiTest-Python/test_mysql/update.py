# -*- coding: UTF-8 -*-

import MySQLdb

# 打开数据库连接
db=MySQLdb.connect('localhost','root','123456','book')

# 使用cursor()方法获取操作游标
cursor = db.cursor()

# SQL 更新语句
sql = "update readerinfo set name='nana' where name='lisa'"
try:
   # 执行SQL语句
   cursor.execute(sql)
   # 提交到数据库执行
   db.commit()
except:
   # 发生错误时回滚
   db.rollback()

# 关闭数据库连接
db.close()