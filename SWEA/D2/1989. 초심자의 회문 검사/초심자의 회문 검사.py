
Test = int(input())

for T in range(Test):
    word = input()
    N = len(word)
    cnt = 0
    for i in range(N//2):
        if word[i] == word[N - i - 1]:
            cnt += 1
        elif word[i] != word[N - i - 1]:
            print(f'#{T+1}', 0)
            break
    if cnt == N//2:
        print(f'#{T + 1}', 1)