import sys;
input = sys.stdin.readline
cnt = Max = 0

for num in sorted([int(input()) for i in range(int(input()))],reverse=True):
    cnt += 1
    Max = max(Max, num * cnt)

print(Max)