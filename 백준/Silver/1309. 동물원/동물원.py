N = int(input())
n0 = n1 = n2 = 1
for n in range(1, N):
    n0, n1, n2 = (n0 + n1 + n2), (n0 + n1), (n0 + n1)
print((n0 + n1 + n2) % 9901)