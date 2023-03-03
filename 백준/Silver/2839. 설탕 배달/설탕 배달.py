N = int(input())
result = 0
while True:
    if N % 5 == 0:
        result += N // 5
        break
    else:
        if N >= 3:
            N -= 3
            result += 1
        else:
            result = -1
            break
    
print(result)