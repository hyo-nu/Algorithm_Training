N = int(input())
q = []
for _ in range(N):
    lst = list(map(int,input().split()))
    q += lst
    q.sort()
    q = q[-N:]
print(q[0])