

score_lst = []
score_dict = {}

for s in range(1,9):
    score = int(input())
    score_lst.append(score)

    score_dict[s] = score

score_lst.sort()
score_dict_sort = sorted(score_dict.items(), key = lambda x: x[1])

print(sum(score_lst[3:]))

score_ord_lst = []
for i in score_dict_sort[3:]:
    score_ord_lst.append(i[0])

score_ord_lst.sort()
for i in score_ord_lst:
    print(i,end=' ')