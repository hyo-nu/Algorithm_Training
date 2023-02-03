Test = int(input())

lst_dict = {}
for T in range(Test):
    old, name = input().split()
    
    if int(old) in lst_dict : lst_dict[int(old)] = lst_dict[int(old)] + [name]
    else : lst_dict[int(old)] = [name]

lst_dict = sorted(lst_dict.items())

for ld in lst_dict:
    for c in range(len(ld[1])):
        print(ld[0],ld[1][c])