import sys;
input = sys.stdin.readline
N, M = map(int,input().split())
dictionary = {}
for _ in range(N):
    word = input().rstrip()
    if (len(word) < M) : continue
    dictionary[word] = dictionary.get(word, 0) + 1

for i in sorted(dictionary.items(), key = lambda x : (-x[1],-len(x[0]),x)):
    print(i[0])