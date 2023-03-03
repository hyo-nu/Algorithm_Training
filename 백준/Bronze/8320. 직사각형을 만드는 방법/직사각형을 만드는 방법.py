n = int(input())
lst = []
for i in range(1, n+1):
    if n % i == 0:
        lst.append(i)
N = len(lst)
cnt = 0
if N % 2 == 0:
    for i in range(1, n // 2 + 1):
        if i == 1:
            cnt += (n // i)
        else:
            square = (n // i)-(i-1)
            if square > 0:
                cnt += square
else:
    for i in range(1, n // 2 + 2):
        if i == 1:
            cnt += (n // i)
        else:
            square = (n // i)-(i-1)
            if square > 0:
                cnt += square
print(cnt)