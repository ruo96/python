import pandas as pd

mydataset = {
  'sites': ["Google", "Runoob", "Wiki"],
  'number': [1, 2,3]
}

myvar = pd.DataFrame(mydataset)

print(myvar)
print(mydataset['number'])
print(mydataset['sites'])

print("============================================")
a = [1, 2, 3]
myvar = pd.Series(a)
print(myvar)
print(myvar[2])
print("============================================")
a = ["Google", "Runoob", "Wiki"]
myvar = pd.Series(a, index = ["x", "y", "z"])
print(myvar)
print(myvar["x"])
print("============================================")
sites = {1: "Google1", 2: "Runoob1", 3: "Wiki1"}
myvar = pd.Series(sites)
print(myvar)
print(myvar[2])
print("============================================")
print("如果我们只需要字典中的一部分数据，只需要指定需要数据的索引即可，如下实例")
sites = {1: "Google", 2: "Runoob", 3: "Wiki"}
index = [1,2]
myvar = pd.Series(sites, index)
print(myvar)
print("============================================")
print("设置 Series 名称参数：")
sites = {1: "Google", 2: "Runoob", 3: "Wiki"}
myvar = pd.Series(sites, index = [1, 2], name="RUNOOB-Series-TEST" )
print(myvar)