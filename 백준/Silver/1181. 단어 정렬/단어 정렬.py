
word_lst = []
Test = int(input())
for T in range(Test):
    word = input()
    word_lst.append(word)
word_lst = list(set(word_lst))
word_lst.sort()
word_lst.sort(key = lambda x:len(x))
for w in word_lst:
    print(w)