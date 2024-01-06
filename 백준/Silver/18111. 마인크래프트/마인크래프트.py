import sys
input = sys.stdin.readline

N, M, B = map(int,input().split())
height_max, height_min = 0, 257
land = [0] * 257

for r in range(N):
    tmp = list(map(int,input().split()))
    for c in range(M):
        land[tmp[c]] += 1
        if height_max < tmp[c] : height_max = tmp[c]
        if height_min > tmp[c] : height_min = tmp[c]

works = []
for height in range(height_min, height_max + 1):
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

print(*sorted(works,key=lambda x : (x[0],-x[1]))[0])