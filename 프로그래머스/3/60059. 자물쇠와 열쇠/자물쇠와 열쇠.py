# key를 회전 시켜야함 (3회전)
# key의 4가지 케이스 전부 완탐
# 이동은?


def solution(key, lock):
    M = len(key) # key 길이
    N = len(lock) # lock 길이
    
    def check(key_rotate, lock):
        for dr in range(-N + 1, N):
            for dc in range(-N + 1, N):
                Open = True
                for r in range(N):
                    for c in range(N):
                        nr, nc = r - dr, c - dc
                        if lock[r][c] == 0:
                            if 0 > nr or M <= nr or 0 > nc or M <= nc or key_rotate[nr][nc] == 0:
                                Open = False
                                break
                        elif lock[r][c] == 1:
                            if 0 <= nr < M and 0 <= nc < M and key_rotate[nr][nc] == 1:
                                Open = False
                                break
                    if not Open : break
                else :
                    print(dr,dc)
                    return True
        return False
            
    result = False
    for _ in range(4):
        key_rotate = list(map(list,zip(*key[::-1])))
        print("key_rotate",key_rotate)
        if check(key_rotate,lock) : 
            result = True
            break
        key = key_rotate
    return result