import sys
input = sys.stdin.readline

def divide_conquer(sr,er,sc,ec):
    global white, blue
    one = zero = 0
    for r in range(sr,er):
        for c in range(sc,ec):
            if G[r][c] == 1 : one += 1
            else : zero += 1

    r_mid = (sr + er) // 2
    c_mid = (sc + ec) // 2
    if one and zero:
        divide_conquer(sr,r_mid,sc,c_mid)
        divide_conquer(sr,r_mid,c_mid,ec)
        divide_conquer(r_mid,er,sc,c_mid)
        divide_conquer(r_mid,er,c_mid,ec)

    if not one : white += 1 ; return
    elif not zero : blue += 1 ; return

N = int(input())
G = [list(map(int, input().split())) for _ in range(N)]
white = blue = 0
divide_conquer(0,N,0,N)
print(white)
print(blue)