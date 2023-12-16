N = int(input())
G = sorted([list(map(int,input().split())) for _ in range(N)])

for lst in G:
    print(*lst)