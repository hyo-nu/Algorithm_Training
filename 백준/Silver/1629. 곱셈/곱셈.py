def power(num, exp, mod):
    if exp == 0:
        return 1
    else :
        x = power(num, exp//2, mod)
        if exp % 2 == 0 :
            return (x * x) % mod
        else :
            return (x * x * num) % mod

A, B, C = map(int,input().split())
print(power(A, B, C))