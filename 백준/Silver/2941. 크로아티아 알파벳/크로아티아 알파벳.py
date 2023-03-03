lst = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
word = input()
N = len(word)
for i in lst:
    if i in word:
        N = N-(len(i)-1)*word.count(i)
if 'dz=' and 'z=' in word:
    N += word.count('dz=')
print(N)