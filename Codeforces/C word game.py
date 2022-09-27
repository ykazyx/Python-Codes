'''C. Word Game
time limit per test1 second
memory limit per test256 megabytes
inputstandard input
outputstandard output
Three guys play a game: first, each person writes down n distinct words of length 3. Then, they total up the number of points as follows:

if a word was written by one person — that person gets 3 points,
if a word was written by two people — each of the two gets 1 point,
if a word was written by all — nobody gets any points.
In the end, how many points does each player have?
Input
The input consists of multiple test cases. The first line contains an integer t (1≤t≤100) — the number of test cases. The description of the test cases follows.

The first line of each test case contains an integer n (1≤n≤1000) — the number of words written by each person.

The following three lines each contain n distinct strings — the words written by each person. Each string consists of 3 lowercase English characters.

Output
For each test case, output three space-separated integers — the number of points each of the three guys earned. You should output the answers in the same order as the input; the i-th integer should be the number of points earned by the i-th guy.'''

t = int(input())
for i in range(t):
    n = int(input())
    p1 = list(input().split())
    p2 = list(input().split())
    p3 = list(input().split())
    ps = p1+ p2 + p3
    s1 = 0
    s2 = 0
    s3 = 0
    counts = dict()
    for nos in ps:
        if nos not in counts:
            counts[nos] = 1
        else:
            counts[nos] += 1
    for j in range(3*n):
        if j < n:
            if counts[ps[j]] == 2:
                s1 += 1
            elif counts[ps[j]] == 1:
                s1 += 3

        elif j < 2 * n:
            if counts[ps[j]] == 2:
                s2 += 1
            elif counts[ps[j]] == 1:
                s2 += 3
        
        elif j < 3 * n:
            if counts[ps[j]] == 2:
                s3 += 1
            elif counts[ps[j]] == 1:
                s3 += 3
    print(s1,s2,s3)
