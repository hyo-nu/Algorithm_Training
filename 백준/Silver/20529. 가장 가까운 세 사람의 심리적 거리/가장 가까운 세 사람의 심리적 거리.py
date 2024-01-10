import sys
from itertools import combinations
from collections import Counter
input = sys.stdin.readline

for test in range(int(input())):
    N = int(input())
    mbtikinds = []
    for mbti, count in Counter(list(input().split())).items():
        if count >= 3 : mbtikinds.extend([mbti] * 3)
        else : mbtikinds.extend([mbti] * count)

    min_distance = 13
    for choice in set(choice for choice in combinations(mbtikinds, 3)):
        choice = list(choice) + [choice[0]]
        total = 0
        for i in range(3):
            distance = 0
            for j in range(4):
                if list(choice[i])[j] != list(choice[i + 1])[j]: distance += 1
            total += distance
            if total > min_distance: break
        min_distance = min(min_distance, total)
        if not min_distance: break
    print(min_distance)