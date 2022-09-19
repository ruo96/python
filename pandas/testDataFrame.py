# -*- coding:utf-8 -*-
import pandas as pd


data = [['Google',10],['Runoob',12],['Wiki',13]]
df = pd.DataFrame(data,columns=['Site','Age'])
print(df)
print("============================================")
print("以下实例使用 ndarrays 创建，ndarray 的长度必须相同， 如果传递了 index，则索引的长度应等于数组的长度。如果没有传递索引，则默认情况下，索引将是range(n)，其中n是数组长度")
data = {'Site':['Google', 'Runoob', 'Wiki'], 'Age':[10, 12,13]}
df = pd.DataFrame(data)
print (df)
print("============================================")
print("还可以使用字典（key/value），其中字典的 key 为列名:  这个里面是可以有空值的")
data = [{'a': 1, 'b': 2},{'a': 5, 'b': 10, 'c': 20}]
df = pd.DataFrame(data)
print (df)
print("============================================")
print("Pandas 可以使用 loc 属性返回指定行的数据，如果没有设置索引，第一行索引为 0，第二行索引为 1，以此类推：")
data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}
# 数据载入到 DataFrame 对象
df = pd.DataFrame(data, index=[2,3,4])
# 返回第一行
print(df.loc[3])
# 返回第二行
print(df.loc[4])
print("============================================")
print("也可以返回多行数据，使用 [[ ... ]] 格式，... 为各行的索引，以逗号隔开")
data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}
# 数据载入到 DataFrame 对象
df = pd.DataFrame(data)
# 返回第一行和第二行
print(df.loc[[0, 1]])
print("============================================")
print("我们可以指定索引值，如下实例：")
data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}
df = pd.DataFrame(data, index = ["day1", "day2", "day3"])
print(df)
print("++++")
print(df.loc["day3"])
print("++++")
print(df.loc["day3"]["duration"])
print("++++")
print(df.loc["day3"]["duration"].dtype)
print("============================================")