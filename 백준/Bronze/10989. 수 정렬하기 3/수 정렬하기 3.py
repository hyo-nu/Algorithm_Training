import sys
num = int(input())
n_lst =[0] * 10001

for _ in range(num):
    n = int(sys.stdin.readline())
    n_lst[n] += 1

for i in range(10001):
    if n_lst[i] != 0:
        for j in range(n_lst[i]):
            print(i)
