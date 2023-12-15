N = int(input())

for i in range(1,N + 1):
    constructor = result = i
    while i:
        constructor += i % 10
        i = i // 10
    if constructor == N : break

print(0 if result == N else result)