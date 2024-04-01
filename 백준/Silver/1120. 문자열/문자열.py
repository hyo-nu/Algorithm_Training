A, B = input().split()
lenA , lenB = len(A), len(B)
Max = 0
for i in range(lenB - lenA + 1):
    cnt = 0
    for j in range(lenA):
        if A[j] == B[i+j]:
            cnt += 1
    Max = max(Max,cnt)

print(lenA - Max)