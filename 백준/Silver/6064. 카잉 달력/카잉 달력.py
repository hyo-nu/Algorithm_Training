import sys
input = sys.stdin.readline

for Test in range(int(input())):
    M, N, x, y = map(int,input().split())
    r = c = order = 0
    year = x
    while True :
        r = (r + year) % M if (r + year) % M else M
        c = (c + year) % N if (c + year) % N else N
        order += year
        year = M
        if r == x and c == y : break
        if order > N * M : break

    print(order if r == x and c == y else -1)