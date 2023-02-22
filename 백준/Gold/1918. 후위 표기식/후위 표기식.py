icp = {'+' : 1, '-' : 1, '*' : 2, '/' : 2, '(' : 3, ')' : 0}
isp = {'+' : 1, '-' : 1, '*' : 2, '/' : 2, '(' : 0, ')' : 0}

calcul = input()
S = []
postfix = ''

for token in calcul:
    if token in icp:
        if token == ')':
            while S[-1] != '(':
                postfix += S.pop()
            S.pop()
        else :
            while S and icp[token] <= isp[S[-1]]:
                postfix += S.pop()
            S.append(token)
    else : postfix += token
while S: postfix += S.pop()

print(postfix)