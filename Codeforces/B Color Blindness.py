'''B. Colourblindness
time limit per test1 second
memory limit per test256 megabytes
inputstandard input
outputstandard output
Vasya has a grid with 2 rows and n columns. He colours each cell red, green, or blue.

Vasya is colourblind and can't distinguish green from blue. Determine if Vasya will consider the two rows of the grid to be coloured the same.

Input
The input consists of multiple test cases. The first line contains an integer t (1≤t≤100) — the number of test cases. The description of the test cases follows.

The first line of each test case contains an integer n (1≤n≤100) — the number of columns of the grid.

The following two lines each contain a string consisting of n characters, each of which is either R, G, or B, representing a red, green, or blue cell, respectively — the description of the grid.

Output
For each test case, output "YES" if Vasya considers the grid's two rows to be identical, and "NO" otherwise.

You can output the answer in any case (for example, the strings "yEs", "yes", "Yes" and "YES" will be recognized as a positive answer).'''

t = int(input())
for i in range(t):
    c = int(input())
    r1 = input()
    r2 = input()
    l = 0
    for j in range(c):
        if (r1[j] == 'R' and (r2[j] == 'G' or r2[j] == 'B')) or ((r1[j] == 'G' or r1[j] == 'B') and r2[j] == 'R' ):
            l = 1
            break
    if l == 0:
        print("YES")
    else:
        print("NO")