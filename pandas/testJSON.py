# -*- coding:utf-8 -*-
import pandas as pd

print("============================================")
df = pd.read_csv('file\\nba.csv')
print(df.to_string())
# print(df)
print(df.columns)
print("============================================")
print("我们也可以使用 to_csv() 方法将 DataFrame 存储为 csv 文件：")
# 三个字段 name, site, age
nme = ["Google", "Runoob", "Taobao", "Wiki"]
st = ["www.google.com", "www.runoob.com", "www.taobao.com", "www.wikipedia.org"]
ag = [90, 40, 80, 98]
# 字典
# dict = {'name': nme, 'site': st, 'age': ag}
# df = pd.DataFrame(dict)
# # 保存 dataframe
# df.to_csv('file\\site.csv')
print("============================================")
print(df.head().to_string())
