list_num = []

for N in range(1,6):
    num = int(input())
    
    if num < 40:
        num = 40
                
    list_num.append(num)

result = sum(list_num)/5
print(round(result))

