import sys
input = sys.stdin.readline

def divide_conquer(sr,sc,n):
    if n == 1:
        return

    for r in range(sr + (n//3), sr + (n//3)*2):
        for c in range( sc + (n//3),  sc + (n//3)*2):
            G[r][c] = " "
    divide_conquer(sr, sc, n // 3) # (0,0)
    divide_conquer(sr, sc + (n//3), n // 3) # (0,1)
    divide_conquer(sr, sc + (n//3)*2, n // 3) # (0,2)
    divide_conquer(sr + (n//3), sc, n // 3) # (1,0)
    divide_conquer(sr + (n//3), sc + (n//3)*2, n // 3) # (1,2)
    divide_conquer(sr + (n//3)*2, sc, n // 3) # (2,0)
    divide_conquer(sr + (n//3)*2, sc + (n//3), n // 3) # (2,1)
    divide_conquer(sr + (n//3)*2, sc + (n//3)*2, n // 3) # (2,2)

N = int(input())
G = [["*"] * N for _ in range(N)]

divide_conquer(0,0,N)

for lst in G:
    print("".join(lst))