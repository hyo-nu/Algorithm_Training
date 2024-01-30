import sys
input = sys.stdin.readline

N = int(input())
G = [list(input().rstrip()) for _ in range(N)]

def divide_conquer(sr, sc, N):
    global ans
    flag = G[sr][sc]
    if N == 1 :
        ans += flag
        return

    for r in range(sr,sr + N):
        for c in range(sc, sc + N):
            if G[r][c] != flag:
                N = N // 2
                ans += "("
                divide_conquer(sr, sc, N) # 왼쪽 위
                divide_conquer(sr, sc + N, N) # 오른쪽 위
                divide_conquer(sr + N, sc, N) # 왼쪽 아래
                divide_conquer(sr + N, sc + N, N) # 오른쪽 아래
                ans += ")"
                return
    ans += flag
    return

ans = ""
divide_conquer(0,0, N,)
print(ans)
