#!/usr/bin/python
# -*- coding:utf-8 -*-


# 已经封装好mysql类了，就不用导入pymsql了，直接导入封装好的类

from dbutil_v2 import Database
# 导包
from dbutil_v2 import Database

# 设置连接数据库的参数
config = {
    "host":"172.20.8.110",
    "port":31002,
    "database":"fedx",
    "charset":"utf8",
    "user":"root",
    "passwd":"Wa@123456"
}

# 实例化时就直接传参数
db = Database(**config)

# 查询1条
select_one = db.select_one("user")
print(select_one)

# 查询多条
select_many = db.select_many(3, "user")
print(select_many)

# 查询所有数据(根据条件)
select_all = db.select_all("user", "id>10")
print(select_all)

# 新增一条数据
db.insert("user","(20,'111')")
# 新增多条数据
db.insert("user", "(21,'123'),(22,'456')")

# 修改一个字段的数据
db.update("user", {"name": "222"}, "id=20")
# 修改多个字段的数据
db.update("user", {"id": "23", "name": "12345"}, "id=103")

# 删除数据
db.delete("user", "id=23")

