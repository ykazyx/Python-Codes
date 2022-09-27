import numpy as np

def retlist(n):
    l = []
    n = str(n)
    for i in n:
        l.append(i)
    return l
def solution(n, b):
    cycle = []
    n = np.base_repr(n, b)
    z = -1
    l = retlist(n)
    k = len(str(n))
    
    while z != n:
        y = int("".join(sorted(l)))
        x = int("".join(sorted(l, reverse=True)))
        z = x - y
        if len(str(z)) != k :
            length = k - len(str(z))
            z = int(str(z) + (length * '0'))

        print(z)
        if z in cycle:
            if z == cycle[-1]:
                return 1
            else:
                return len(cycle) - (cycle.index(z))
        else:
            cycle.append(z)
        l = retlist(z)


n = int(input("Enter a nonnegative integer with '2 <= length <= 9' : "))
b = int(input("Base(>=2 and <=10): "))
sol = solution(n,b)
print(sol)