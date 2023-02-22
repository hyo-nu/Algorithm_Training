month, day = map(int,input().split())

day31_lst = [1,3,5,7,8,10,12]
day30_lst = [4,6,9,11]
day28_lst = [2]
day_lst = ['SUN','MON','TUE','WED','THU','FRI','SAT']

total_date = 0
for m in range(0,month):
    if m == 0 : pass
    elif m in day31_lst : total_date += 31
    elif m in day30_lst : total_date += 30
    elif m in day28_lst : total_date += 28
total_date += day

print(day_lst[total_date % 7])

