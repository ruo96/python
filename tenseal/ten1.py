# -*- coding:utf-8 -*-
import tenseal as ts

a = 1
print(a)
context = ts.context(ts.SCHEME_TYPE.BFV, poly_modulus_degree=4096, plain_modulus=1032193)
print(context)
#Êä³ö£º<tenseal.enc_context.Context object at 0x7f380e2872b0>