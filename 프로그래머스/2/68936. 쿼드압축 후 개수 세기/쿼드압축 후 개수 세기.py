def solution(arr):
    def divide_conquer(sr, sc, n):
        if n == 1:
            result[arr[sr][sc]] += 1
            return
        else:
            for r in range(sr, sr + n):
                for c in range(sc, sc + n):
                    if arr[sr][sc] != arr[r][c]:
                        divide_conquer(sr, sc, n // 2)
                        divide_conquer(sr, sc + n // 2, n // 2)
                        divide_conquer(sr + n // 2, sc, n // 2)
                        divide_conquer(sr + n // 2, sc + n // 2, n // 2)
                        return
            else:
                result[arr[sr][sc]] += 1
                return
        
    N = len(arr)
    result = [0, 0]
    divide_conquer(0, 0, N)
    return result