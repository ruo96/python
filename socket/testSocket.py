# socket()函数
#
# Python 中，我们用 socket（）函数来创建套接字，语法格式如下：
#
# socket.socket([family[, type[, proto]]])
#
# 参数
#
#     family: 套接字家族可以使 AF_UNIX 或者 AF_INET。
#     type: 套接字类型可以根据是面向连接的还是非连接分为 SOCK_STREAM 或 SOCK_DGRAM。
#     protocol: 一般不填默认为 0。

# !/usr/bin/python
# -*- coding: UTF-8 -*-
# 文件名：server.py

import socket  # 导入 socket 模块

s = socket.socket()  # 创建 socket 对象
host = socket.gethostname()  # 获取本地主机名
port = 12345  # 设置端口
s.bind((host, port))  # 绑定端口

s.listen(5)  # 等待客户端连接
while True:
    c, addr = s.accept()  # 建立客户端连接
    print('连接地址：', addr)
    c.send('欢迎访问菜鸟教程！')
    c.close()  # 关闭连接