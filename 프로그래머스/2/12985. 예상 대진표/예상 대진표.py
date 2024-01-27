def solution(n,a,b):
    r = 1
    while 2 ** r < n : r += 1
    
    a, b = min(a, b), max(a, b)
    sp, ep = 1, n
    n = n // 2
    
    while True:
        if sp <= a < sp + n and sp + n <= b <= ep:
            break
        
        elif sp <= a < sp + n and sp <= b < sp + n:
            r -= 1
            ep = sp + n - 1
            n = n // 2
        
        elif sp + n <= a <= ep and sp + n <= b <= ep:
            r -= 1
            sp = sp + n
            n = n // 2
    
    return r