N = int(input())
M = int(input())
S = input()
check_len = 2 * N + 1
check = 'IO' * N +'I'
cnt = 0
for i in range(M-check_len+1):
    if S[i] == 'I':
        if S[i:i+check_len] == check :
            cnt+=1
print(cnt)