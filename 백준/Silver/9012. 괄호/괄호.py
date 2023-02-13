def push(item):
    global top
    top += 1
    S[top] = item

def pop():
    global top
    top -= 1

Test = int(input())

for T in range(Test):
    bracket = input()
    top = -1
    S = [0] * len(bracket)
    good = 0
    for i in bracket:
        if top == -1 : push(i)
        elif i == '(' : push(i)
        elif i == ')':
            if S[top] == '(' : pop()
            elif S[top] == ')':
                break
    else:
        good += 1

    if top >= 0 or good == 0 : print('NO')
    elif good == 1 : print('YES')
