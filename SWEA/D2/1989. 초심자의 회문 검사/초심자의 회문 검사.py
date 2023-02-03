Test = int(input())

for T in range(Test):
    word = input()
    count = 0
    for w in range(len(word)//2):
        if word[w] != word[len(word)-w-1]:
            count += 1   
    if count == 0 : print(f'#{T+1} 1')
    else : print(f'#{T+1} 0')