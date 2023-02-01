# -*- coding:utf-8 -*-
import tenseal as ts
from decimal import Decimal

# Setup TenSEAL context
context = ts.context(
            ts.SCHEME_TYPE.CKKS,    #  方案类型
            poly_modulus_degree=8192,    # 模多项式的级数
            coeff_mod_bit_sizes=[60, 40, 40, 60]   # 模多项式的系数模数
          )
context.generate_galois_keys()
context.global_scale = 2**40

v1 = [2, 9, 2, 3, 4]
v2 = [4, 7, 3, 6, 7]


# encrypted vectors【编码和加密】
enc_v1 = ts.ckks_vector(context, v1) 
enc_v2 = ts.ckks_vector(context, v2)

# 密文+密文
result = enc_v1 * enc_v2 - enc_v1
result.decrypt() # ~ [4, 4, 4, 4, 4]
print(result.decrypt())  # 不能 转实数

# print(Decimal((result_ori).decrypt()[1]).quantize(Decimal("0.00")))

print("============================================")




