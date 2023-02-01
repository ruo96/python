# -*- coding:utf-8 -*-

import tenseal as ts

c  = 10.1234
print("%.2f" % c)

print(c)

import numpy as np

plain1 = ts.plain_tensor([1,2,3,4], [2,2])
print(" First tensor: Shape = {} Data = {}".format(plain1.shape, plain1.tolist()))

plain2 = ts.plain_tensor(np.array([5,6,7,8]).reshape(2,2))
print(" Second tensor: Shape = {} Data = {}".format(plain2.shape, plain2.tolist()))

# 输出：
# First tensor: Shape = [2, 2] Data = [[1.0, 2.0], [3.0, 4.0]]
# Second tensor: Shape = [2, 2] Data = [[5.0, 6.0], [7.0, 8.0]]

