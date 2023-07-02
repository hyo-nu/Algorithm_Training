words = list(input().strip())
bomb = list(input().strip())

S = []
for word in words:
    S += word
    cnt = 0
    if word == bomb[-1]:
        if bomb == S[-len(bomb):]:
            while cnt < len(bomb):
                S.pop()
                cnt += 1

print(''.join(S)) if S else print('FRULA')