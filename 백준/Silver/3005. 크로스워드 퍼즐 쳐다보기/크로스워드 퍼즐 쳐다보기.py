def puzzle(arr):
    for lst in arr:
        tmp = ''
        for word in lst:
            if word == '#':
                if len(tmp) >= 2: result.append(tmp)
                tmp = ''
            else:
                tmp += word
        if len(tmp) >= 2: result.append(tmp)

R, C = map(int,input().split())
G = [input() for _ in range(R)]
G_T = list(map(list,zip(*G)))
result = []
puzzle(G)
puzzle(G_T)
print(sorted(result)[0])