N = int(input())
N_nums = list(map(int,input().split()))

M = int(input())
M_nums = list(map(int,input().split()))

result_dict = {}
for n in range(len(N_nums)):
    result_dict[N_nums[n]] = 0

for m in M_nums:
    if m not in result_dict:
        print(0, end = ' ')
    else :
        print(1,end = ' ')
        

        