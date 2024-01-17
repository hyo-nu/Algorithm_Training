from math import lcm

f_hour = input()
s_hour = input()
f_cycle = input()
s_cycle = input()

fh = int(f_hour[0:2])*60 + int(f_hour[3:])  # 첫 번째 별 시간
sh = int(s_hour[0:2])*60 + int(s_hour[3:])  # 두 번째 별 시간
fc = int(f_cycle[0:2])*60 + int(f_cycle[3:])  # 첫 번째 별 주기
sc = int(s_cycle[0:2])*60 + int(s_cycle[3:])  # 두 번째 별 시간

weekday = ['Saturday', 'Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
result, cnt, llcm = 0, 0, lcm(fc, sc)  # llcm-> 최소공배수

while cnt <= llcm:
    if sh == fh:break  # 별이 반짝이는 시간이 일치하면
    if fh > sh:
        sh += sc
    else:
        fh += fc
    cnt += 1

result = fh
if cnt > llcm:print('Never')
else:
    print(weekday[(result//60)//24 % 7])
    hh = str((result//60) % 24)
    mm = str(result % 60)
    print('0'*(2-len(hh)) + hh + ':' + '0'*(2-len(mm)) + mm)