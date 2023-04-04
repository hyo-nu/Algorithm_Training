while True:
    S = input()
    if S == '0':break
    S_lst = list(S)
    S_lst.reverse()
    if S == ''.join(S_lst): print('yes')
    else:print('no')
