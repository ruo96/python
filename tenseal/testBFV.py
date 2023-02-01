# -*- coding:utf-8 -*-
import tenseal as ts
from decimal import Decimal
from time import time

# Setup TenSEAL context
# context = ts.context(
#             ts.SCHEME_TYPE.CKKS,
#             poly_modulus_degree=8192,
#             coeff_mod_bit_sizes=[60, 40, 40, 60]
#           )
context = ts.context(ts.SCHEME_TYPE.BFV, poly_modulus_degree=4096, plain_modulus=1032193)

context.generate_galois_keys()
context.global_scale = 2**40

v1 = [0, 1, 2, 3, 4]
# v1 = [0.0, 1.0, 2.0, 3.0, 4.0]
v2 = [4, 7, 3, 6, 7]
# v2 = [4.0, 3.0, 2.0, 1.0, 0.0]

# encrypted vectors【编码和加密】
enc_v1 = ts.bfv_vector(context, v1)
enc_v2 = ts.bfv_vector(context, v2)

# 密文+密文
result = enc_v1 + enc_v2
result_ori = enc_v1 + v2
result.decrypt() # ~ [4, 4, 4, 4, 4]
print(result.decrypt())  #
print("origin")
print((result_ori).decrypt())
print(Decimal((result_ori).decrypt()[1]).quantize(Decimal("0.00")))

print("=====================2=======================")

# 点积：<密文,密文>
result = enc_v1.dot(enc_v2)
print(result.decrypt()) # ~ [10]
print("origin")
result_ori  = enc_v1.dot(v2)
print(result_ori.decrypt())
print("=======================3=====================")

matrix = [
  [73, 5, 8],
  [81, -5, 66],
  [-100, -78, -2],
  [0, 9, 17],
  [69, 11, 10],
]
# 密文向量*明文矩阵

print("======================4======================")

context = ts.context(ts.SCHEME_TYPE.BFV, poly_modulus_degree=4096, plain_modulus=1032193)
print(context)

public_context = ts.context(ts.SCHEME_TYPE.BFV, poly_modulus_degree=4096, plain_modulus=1032193)
print("Is the context private?", ("Yes" if public_context.is_private() else "No"))  #  私钥为不空返回 True
print("Is the context public?", ("Yes" if public_context.is_public() else "No"))    #  私钥为空返回 True

sk = public_context.secret_key()# 暂存私钥

# the context will drop the secret-key at this point，删除私钥
public_context.make_context_public()
print("Secret-key dropped")
print("Is the context private?", ("Yes" if public_context.is_private() else "No"))
print("Is the context public?", ("Yes" if public_context.is_public() else "No"))

# 输出：
# Is the context private? Yes
# Is the context public? No
# Secret-key dropped
# Is the context private? No
# Is the context public? Yes

print("============================================")
plain_vector = [60, 66, 73, 81, 90]
encrypted_vector = ts.bfv_vector(context, plain_vector)
add_vector =[1,2,3,4,5]
result = encrypted_vector + add_vector
print("enc is:", result.size())

print("We just encrypted our plaintext vector of size:", encrypted_vector.size())
print(result.decrypt())

print("============================================")





