def solution(n, k):
    def conversion(n, k):
        value = ""
        while n :
            value += str(n % k)
            n = n // k
        return str(value[::-1])
    
    def isPrime(num):
        for i in range(2,int(num ** 0.5) + 1):
            if not num % i : return False
        return True
    
    change = conversion(n, k)
    number = ""
    prime_cnt = 0
    
    for i in range(len(change)):
        
        if change[i] != "0":
            number += change[i]
            
        elif number and number != "1":
            if isPrime(int(number)): 
                prime_cnt += 1
            number = ""
        elif number and number == "1":
            number = ""
            
    if number and number != "1":
        if isPrime(int(number)): 
            prime_cnt += 1
            
    return prime_cnt