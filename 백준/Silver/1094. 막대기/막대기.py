x = int(input())

stick = 64
stick_len = 0
stick_cnt = 0

while x != stick_len:

    if x < stick_len + stick / 2:
        stick = stick / 2
    elif x >= stick_len + stick / 2:
        stick_len += stick / 2
        stick_cnt += 1

if x == 64: # 64cm를 원해서 막대를 자를 필요가 없음
    stick_cnt = 1

print(stick_cnt)