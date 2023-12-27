def solution(n, t, m, p):
    code = {10:"A",11:"B",12:"C",13:"D",14:"E",15:"F"}
    
    def n_decimal(num, n):
        value = ""
        while num:
            value += code.get(num % n,str(num % n))
            num //= n
        return value[::-1]
    
    total = "0"
    for i in range(t * m):
        total += n_decimal(i, n)
        
    result = ""
    for i in range(t):
        result += total[i * m + p - 1]

    return result


