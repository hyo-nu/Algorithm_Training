def f(x):
    total = 1
    for i in x:
        total *= int(i)
    return total


num = input()
idx = 1
while True:
    if idx == len(num):
        idx = 'NO'
        break
    if f(num[:idx]) == f(num[idx:]):
        idx = 'YES'
        break
    idx += 1
print(idx)