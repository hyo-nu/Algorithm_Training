icp = ['+', '-', '*', '/']

N = int(input())
calcul = input()

operand = [int(input()) for _ in range(N)] #[1,2,3,4,5]

S = []
for token in calcul:
    if token in icp:
        b = S.pop()
        if type(b) == str: b = operand[ord(b)-65]
        a = S.pop()
        if type(a) == str: a = operand[ord(a) - 65]

        if token == '+' : S.append(a + b)
        elif token == '-': S.append(a - b)
        elif token == '*': S.append(a * b)
        elif token == '/': S.append(a / b)
    else:
        S.append(token)
print(format(S[0], ".2f"))