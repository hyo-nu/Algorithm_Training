n = int(input())
for i in range(n * 2 - 1):
    if i >= n :
        i = i - (i - (n - 1)) * 2
    print(" " * (n - 1 - i), end="")
    print("*" * (2 * i + 1))