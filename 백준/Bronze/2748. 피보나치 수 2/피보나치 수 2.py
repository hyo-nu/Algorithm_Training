n = int(input())
d0, d1 = 0, 1
for i in range(n-1):
    d0, d1 = d1, d0 + d1

print(d1)
