import sys
input = sys.stdin.readline

N, M = map(int,input().split())

number_dict, name_dict = {}, {}
for i in range(1, N+1):
    poketmon = input().rstrip()
    number_dict[i] = number_dict.get(i,poketmon)
    name_dict[poketmon] = name_dict.get(poketmon,i)

for _ in range(M):
    problem = input().rstrip()
    if problem.isdigit():
        print(number_dict[int(problem)])
    else:
        print(name_dict[problem])
