def matrix_mul(left, right, mod):
    matrix = []
    for lst1 in left:
        tmp = []
        for lst2 in list(zip(*right)):
            tmp.append(sum([a*b for a, b in zip(lst1,lst2)]) % mod)
        matrix.append(tmp)
    return matrix

def power(matrix, exp):
    if exp <= 1 :
        return [(1,1),(1,0)]
    else :
        x = power(matrix, exp // 2)
        mul = matrix_mul(x,x,mod)
        if exp % 2 == 0:
            return mul
        else:
            return matrix_mul(matrix, mul, mod)

N = int(input())
matrix = [(1,1),(1,0)]
mod = 1000000
print(power(matrix, N - 1)[0][0])