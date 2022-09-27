f = open("second_hands_input.txt")
file = f.readlines()
l = []
for lines in file :
    lines = lines.rstrip()
    l.append(lines)

cmt = 1
cnt = 2
for i in range(int(l[0])):
    counts = dict()
    n,k  = map(int, l[cmt].split())
    s = map(int, l[cnt].split())
    print(n,k,s)
    for nos in s:
        if nos not in counts:
            counts[nos] = 1
        else:
            counts[nos] += 1

    cnt1 = max(set(s), key = s.count)
    cnt2 = s.count(cnt1)
    if 2 * k  < n :
        print(f"Case #{i+1}: NO")
    elif cnt2 > 2 :
        print(f"Case #{i+1}: NO")
    else:
        print(f"Case #{i+1}: YES")


    cnt += 2
    cmt += 2


