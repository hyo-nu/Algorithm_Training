# 5 <= s <= 1,000,000
# 1 <= 튜플의 원소 <= 100,000
# 1 <= 리턴값길이 <= 500
from collections import Counter

def solution(s):
    
    arr = []
    for S in s.lstrip("{{").rstrip("}}").split("},{"):
        arr += list(map(int,S.split(",")))
    
    result = []
    for key, value in sorted(Counter(arr).items(), key = lambda x : -x[1]):
        result.append(key)

    return result
