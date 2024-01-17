class Trie:
    def __init__(self):
        self.child = dict()
        self.count = 0
        
    def insert(self, str):
        curr = self
        for ch in str:
            curr.count += 1
            if ch not in curr.child:
                curr.child[ch] = Trie()
            
            curr = curr.child[ch]
        curr.count += 1
        
    def search(self, str):
        curr = self
        for ch in str:
            if ch == "?":
                return curr.count
            if ch not in curr.child:
                return 0
            curr = curr.child[ch]
        return curr.count

def solution(words, queries):
    TrieRoot = [Trie() for _ in range(10000)]
    ReTrieRoot = [Trie() for _ in range(10000)]
    answer = []
    
    for str in words:
        TrieRoot[len(str)-1].insert(str)
        ReTrieRoot[len(str)-1].insert(str[::-1])
    
    for str in queries:
        if str[0] != "?":
            answer.append(TrieRoot[len(str)-1].search(str))
        else:
            answer.append(ReTrieRoot[len(str)-1].search(str[::-1]))
    
    return answer



# from bisect import bisect_left, bisect_right

# def solution(words, queries):
#     answer = []
#     data = [[] for _ in range(10001)] 
#     reverse = [[] for _ in range(10001)]
    
#     def count_by_range(diect,q, a, left_value, right_value):
#         left_index = bisect_left(a, left_value)
#         right_index = bisect_right(a, right_value)
#         return right_index - left_index   
    
#     for word in words:
#         data[len(word)].append(word)
#         reverse[len(word)].append(word[::-1])
    
#     for i in range(10001):
#         data[i].sort()
#         reverse[i].sort()
    
#     for q in queries:
#         if q[0] != "?":
#             res = count_by_range("정방향",q, data[len(q)], q.replace("?","a"), q.replace("?","z"))
#         else:
#             res = count_by_range("역방향",q, reverse[len(q)], q[::-1].replace("?","a"), q[::-1].replace("?","z"))
#         answer.append(res)
#     return answer
