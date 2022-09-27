ls = []
n = int(input())


for i in range(n):
    ls.append(input())

for i in ls:
    l = len(i)
    if l > 10:
        print(f"{i[0]}{l - 2}{i[l - 1]}")
    else:
        print(i)