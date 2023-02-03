num = int(input())
num = list(map(int,list(str(num))))
sum = 0

for c in num:
    sum += c

print(sum)
