num = int(input())
sum = 0

for c in range(1,num+1):
    sum += c
    if sum > num:
        result = c-1
        break
    elif sum == num:
        result = c
        break
print(result)
            