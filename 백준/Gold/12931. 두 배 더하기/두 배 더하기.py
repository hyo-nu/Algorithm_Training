import sys;
input = sys.stdin.readline

N = int(input())
lst = list(map(int,input().split()))

count = 0
while True:
    zero = 0
    for i in range(N):
        if lst[i] % 2 :
            lst[i] = (lst[i] - 1) / 2 ; count += 1
        elif lst[i] % 2 == 0 : lst[i] /= 2
        if lst[i] == 0 : zero += 1
    count += 1
    if zero == N : break

print(count-1)