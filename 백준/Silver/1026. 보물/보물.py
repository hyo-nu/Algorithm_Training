import sys;
input = sys.stdin.readline

n = int(input())
a = sorted(list(map(int,input().split())))
b = sorted(list(map(int,input().split())), reverse = True)
Min = 0
for i in range(n):
    Min += (a[i] * b[i])
print(Min)