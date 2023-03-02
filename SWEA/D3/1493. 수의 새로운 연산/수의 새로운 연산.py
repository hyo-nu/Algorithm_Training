def find_RC(point):
    for r in range(1,200):
        for c in range(1,200):
            if Map[r][c] == point:
                return (r,c)
Test = int(input())

for TC in range(Test):
    Map = [[0]*300 for _ in range(300)]
    for r in range(1,300):
        Map[r][1] = Map[r-1][1] + r
    for r in range(1,300):
        num = r
        for c in range(2,300):
            Map[r][c] = Map[r][c-1] + num
            num+=1

    p, q = map(int, input().split())
    r1,c1 = find_RC(p)
    r2,c2 = find_RC(q)
    print(f'#{TC+1}',Map[r1+r2][c1+c2])

