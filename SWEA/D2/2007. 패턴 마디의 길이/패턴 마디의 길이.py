Test = int(input())

for T in range(Test):
    string = input()
    for s in range(1,len(string)+1):
        if string[0:s] == string[s:s*2]:
            print(f'#{T+1} {s}')
            break
        else:
            pass