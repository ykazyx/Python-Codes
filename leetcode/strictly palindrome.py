import numpy as np
nos = int(input())
change = "true"
for i in range(2, nos - 1):
    ternary=str(np.base_repr(nos,base = i))
    rev = list(reversed(ternary))
    print(list(ternary), rev)
    if list(ternary) != rev:
        change = "false"
        break
    
print(change)