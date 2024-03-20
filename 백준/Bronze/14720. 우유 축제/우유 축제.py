import sys;
input = sys.stdin.readline
n = int(input())
store = list(map(int, input().split()))
cnt = 0
for i in range(n):
    if store[i] == cnt % 3:
        cnt += 1
print(cnt)
