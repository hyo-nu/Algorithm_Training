N = int(input())
start = N - 9 * len(str(N))

for num in range(start if start > 0 else 0, N + 1):
    constructor = num
    if constructor + sum(list(map(int,list(str(num))))) == N : break

print(0 if constructor == N else constructor)