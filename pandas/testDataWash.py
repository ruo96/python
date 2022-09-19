# -*- coding:utf-8 -*-
import pandas as pd

print("包含了四种空数据：    n/a   NA    —    na")


print("============================================")
print('''
#如果我们要删除包含空字段的行，可以使用 dropna() 方法，语法格式如下：
#DataFrame.dropna(axis=0, how='any', thresh=None, subset=None, inplace=False)
参数说明：

    axis：默认为 0，表示逢空值剔除整行，如果设置参数 axis＝1 表示逢空值去掉整列。
    how：默认为 'any' 如果一行（或一列）里任何一个数据有出现 NA 就去掉整行，如果设置 how='all' 一行（或列）都是 NA 才去掉这整行。
    thresh：设置需要多少非空值的数据才可以保留下来的。
    subset：设置想要检查的列。如果是多个列，可以使用列名的 list 作为参数。
    inplace：如果设置 True，将计算得到的值直接覆盖之前的值并返回 None，修改的是源数据。

我们可以通过 isnull() 判断各个单元格是否为空。
''')
df = pd.read_csv('file\\property-data.csv')
print(df.to_string())
missing_values = ["n/a", "na", "--"]
df = pd.read_csv('file\\property-data.csv', na_values = missing_values)

print (df['NUM_BEDROOMS'])
print (df['NUM_BEDROOMS'].isnull())
print("============================================")
print("我们也可以移除指定列有空值的行：")
df = pd.read_csv('file\\property-data.csv')
df.dropna(subset=['ST_NUM'], inplace = True)
print(df.to_string())
print("============================================")
print(''' 
如果我们要清洗重复数据，可以使用 duplicated() 和 drop_duplicates() 方法。
如果对应的数据是重复的，duplicated() 会返回 True，否则返回 False。''')
person = {
  "name": ['Google', 'Runoob', 'Runoob', 'Taobao'],
  "age": [50, 40, 40, 23]
}
df = pd.DataFrame(person)

print(df.duplicated())
print(df.count())
# print(df.mean())
print("========== ==================================")
