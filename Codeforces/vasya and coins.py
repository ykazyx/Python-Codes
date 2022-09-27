ml = []
for _ in range(int(input())):
    l = ""
    l = input()
    ml.append(l.split())


for i in ml:

    i[0] = int(i[0])
    i[1] = int(i[1])

    if i[0] == 0:
        print(1)

    elif i[0] > 0 and i[1] == 0:
        print((i[0]*1) + 1)

    elif i[0] > 0 and i[1] > 0:
        print ((i[0] + i[1] * 2) + 1)
