import sys;
from collections import deque
input = sys.stdin.readline

N = int(input())
a, b = 2, 1
result = []
while a != b:
    value = (a+b) * (a-b)
    if value < N : a += 1
    elif value > N : b += 1
    elif value == N :
        b += 1
        result.append(a)

if result :
    for i in result: print(i)
else:
    print(-1)