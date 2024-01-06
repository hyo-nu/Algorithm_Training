import sys
input = sys.stdin.readline

N, M, B = map(int,input().split())
land = [0] * 257

for _ in range(N):
    for value in map(int,input().split()):
        land[value] += 1

works = []
for height in range(256,-1,-1):
    time = 0
    block = B
    for i in range(257):
        if land[i] and i > height:
            time = time + (i - height) * land[i] * 2
            block = block + (i - height) * land[i]

        elif land[i] and i < height:
            time = time + (height - i) * land[i]
            block = block - (height - i) * land[i]

    if block >= 0 :
        works.append((time,height))

print(*sorted(works,key=lambda x : x[0])[0])