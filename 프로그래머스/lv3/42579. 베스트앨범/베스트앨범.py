def solution(genres, plays):
    dic1 = {i: 0 for i in set(genres)}
    dic2 = {i: [] for i in set(genres)}
    for i in range(len(genres)):
        dic1[genres[i]] += plays[i]
        dic2[genres[i]] += [(plays[i], i)]

    lst = []
    for i,_ in sorted(dic1.items(), key=lambda x:x[1],reverse=True):
        d = sorted(dic2[i],key=lambda x:x[0] ,reverse=True)
        print(d)
        if len(d) == 1:
            lst += [d[0][1]]
        else:
            lst += [d[0][1]] + [d[1][1]]
    return lst
#     genres_set = list(set(genres))
#     elbum = {genres_set[i]:[] for i in range(len(genres_set))}
#     elbum_rank = {genres_set[i]:0 for i in range(len(genres_set))}
    
#     for i in range(len(genres)):
#         elbum[genres[i]].append([plays[i],i])
#         elbum_rank[genres[i]] += plays[i]
    
#     tmp = []
#     for K,V in elbum_rank.items():
#         tmp.append((K,V))
#     tmp.sort(key = lambda x : x[1],reverse=True)
    
#     result = []
#     for lst in tmp:
#         elbum[lst[0]].sort(key = lambda x : x[0],reverse=True)
#         if len(elbum[lst[0]]) == 1:
#             result.append(elbum[lst[0]][0][1])
#         else:
#             for i in range(2):
#                 result.append(elbum[lst[0]][i][1])

#     return result
