f = open("consecutive_cuts_chapter_1_validation_input.txt")
file = f.readlines()
l = []
cnt = 0


for lines in file :
    lines = lines.rstrip()
    s = list(map(int, lines.split()))
    l.append(lines)

cnkt = 1
cat = 2
cbt = 3
ans = []
for i in range(int(l[0])):
    n,k  = map(int, l[cnkt].split())
    a = list(map(int, l[cat].split()))
    b = list(map(int, l[cbt].split()))
    if a == b:
        ans += [f"Case #{i+1}: YES"]
    elif k == 0:
        ans += [f"Case #{i+1}: NO"]
    else :
        afirst = a[0]
        bfirst = b[0]
        tofind = a.index(bfirst)
        # for j in range(n):
        # c = a[j + 1 : ] + a[0 : j + 1] 
        c = a[tofind : ] + a[0 : tofind] 
        if c == b:
            # print(c)
            # print(b)
            ans += [f"Case #{i+1}: YES"]
            # break 
    try:
        amb = ans[i]
    except:
        ans += [f"Case #{i+1}: NO"]


    cnkt += 3
    cat += 3
    cbt += 3
    print(ans[i])

for m in ans:
    with open('ans.txt', 'a') as f:
        f.write(m + '\n')
