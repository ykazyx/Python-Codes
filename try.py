# a = input()

# # # # Base 16(hexadecimal)
# # # # hex_a = hex(a)
# # # # print(hex_a)s
# print(int(a, 3))

import numpy as np

number=int(input()) # decimal
ternary=np.base_repr(number,base=2)
print(ternary)

# list = [1,2,3,4,5]
# print(list[-1])