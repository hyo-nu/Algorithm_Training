num = int(input())

result = []

for c in range(2,num+1):
    
    while num % c == 0:
        num = num // c
        print(c)
    
    