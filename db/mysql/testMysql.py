#!/usr/bin/python
# -*- coding:utf-8 -*-


# 已经封装好mysql类了，就不用导入pymsql了，直接导入封装好的类

from dbutil import Mysqldb

# 实例化
my_db = Mysqldb()

# 写查询SQL语句
sql = "select * from user"
# 查询所有
select_all = my_db.select_all(sql)
print("查询所有数据：\n", select_all)
# 查询一条
select_one = my_db.select_one(sql)
print("查询一条数据：\n", select_one)
# 查询多条
select_many = my_db.select_many(sql, 3)
print("查询3条数据：\n", select_many)

# 新增一条数据
value = (16, 'BBQ')
sql = f"insert into user values {value}"
insert_one = my_db.commit_data(sql)
# 新增多条数据
values = "(17, 'aaa'), (18, 'bbb'), (19, 'ccc')"
sql = f"insert into user values {values}"
insert_many = my_db.commit_data(sql)

# 修改数据
sql = "update user set name = '出不去了' where id = 1700"
my_db.commit_data(sql)

# 删除数据
sql = "delete from user where id = 1700"
my_db.commit_data(sql)
