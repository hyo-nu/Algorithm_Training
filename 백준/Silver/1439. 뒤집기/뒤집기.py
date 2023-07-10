S = list(input())

i, count = 1, 0
while i < len(S):
    if S[i] != S[i - 1]:
        count += 1
        while i < len(S) and S[i] != S[i-1]:
            S[i] = S[i-1]
            i += 1
    i += 1
print(count)