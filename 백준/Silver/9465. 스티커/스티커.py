import sys
input = sys.stdin.readline

for test in range(int(input())):
    n = int(input())
    s1 = list(map(int,input().split()))
    s2 = list(map(int,input().split()))

    for c in range(1,n):
        s1_now, s2_now = s1[c],s2[c]
        s1[c], s2[c] = s1[c] + s2[c-1], s2[c] + s1[c-1]
        if c >= 2:
            s1[c] = max(s1[c], s1[c-2]+s1_now, s2[c-2]+s1_now)
            s2[c] = max(s2[c], s1[c-2]+s2_now, s2[c-2]+s2_now)

    print(max(s1[n-1],s2[n-1]))