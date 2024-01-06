import sys
input = sys.stdin.readline

L, S = int(input()), list(input().rstrip())
value = 0
for i, s in enumerate(S):
    value = value + (ord(s)-96) * (31 ** i)
print(value % 1234567891)