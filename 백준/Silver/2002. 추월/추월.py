import sys;
input = sys.stdin.readline

N = int(input())
carorder = {}
count = 0
for i in range(N):
    car = input().rstrip()
    carorder[car] = i

out = [input().rstrip() for i in range(N)]
for i in range(N):
    for j in range(i+1,N):
        if carorder[out[i]] > carorder[out[j]]:
            count += 1
            break

print(count)