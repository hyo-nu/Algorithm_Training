import sys
from itertools import combinations

input = sys.stdin.readline
N, K = map(int,input().split())
lst = [i for i in range(1,N + 1)]
print(len(list(combinations(lst,K))))
