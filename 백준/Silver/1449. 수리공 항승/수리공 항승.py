N, L = map(int,input().split())
lst = sorted(list(map(int,input().split())))

cnt = 0
length = 0
for l in lst:
    if length < l:
        cnt += 1
        length = l + L - 1
print(cnt)
