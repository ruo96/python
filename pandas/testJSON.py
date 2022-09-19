# -*- coding:utf-8 -*-
import pandas as pd
import json
from glom import glom



df = pd.read_json('file\\site.json')

print(df.to_string())

print("============================================")
print("to_string() 用于返回 DataFrame 类型的数据，我们也可以直接处理 JSON 字符串")
data =[
    {
      "id": "A001",
      "name": "菜鸟教程",
      "url": "www.runoob.com",
      "likes": 61
    },
    {
      "id": "A002",
      "name": "Google",
      "url": "www.google.com",
      "likes": 124
    },
    {
      "id": "A003",
      "name": "淘宝",
      "url": "www.taobao.com",
      "likes": 45
    }
]
df = pd.DataFrame(data)
print(df)
print("============================================")
print("JSON 对象与 Python 字典具有相同的格式，所以我们可以直接将 Python 字典转化为 DataFrame 数据：")
# 字典格式的 JSON
s = {
    "col1":{"row1":1,"row2":2,"row3":3},
    "col2":{"row1":"x","row2":"y","row3":"z"}
}

# 读取 JSON 转为 DataFrame
df = pd.DataFrame(s)
print(df)
print("============================================")
print("从 URL 中读取 JSON 数据：")
URL = 'https://static.runoob.com/download/sites.json'
df = pd.read_json(URL)
print(df)
print("============================================")
print("假设有一组内嵌的 JSON 数据文件 nested_list.json ：")
df = pd.read_json('file\\nest_list.json')

print(df)
print("============================================")
print("这时我们就需要使用到 json_normalize() 方法将内嵌的数据完整的解析出来")
# 使用 Python JSON 模块载入数据
with open('file\\nest_list.json','r') as f:
    data = json.loads(f.read())

# 展平数据
df_nested_list = pd.json_normalize(data, record_path =['students'])
print(df_nested_list)

# 展平数据
df_nested_list = pd.json_normalize(
    data,
    record_path =['students'],
    meta=['school_name', 'class']
)
print(df_nested_list)
print("============================================")
print("我们需要使用到 glom 模块来处理数据套嵌，glom 模块允许我们使用 . 来访问内嵌对象的属性。")
df = pd.read_json('file\\nest_deep.json')

data = df['students'].apply(lambda row: glom(row, 'grade.math'))
print(data)
print("============================================")