
v_num = int(input())
v_who = list(input())

A_num = 0
B_num = 0

for c in v_who:
    if c == 'A':
        A_num += 1
    elif c == 'B':
        B_num += 1

if A_num > B_num:
    print('A')
elif A_num < B_num:
    print('B')
else:
    print('Tie')