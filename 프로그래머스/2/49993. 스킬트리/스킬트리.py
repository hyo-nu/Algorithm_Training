def solution(skill, skill_trees):
    
    cnt = 0
    for tree in skill_trees:
        def isPosible(tree):
            for i in range(len(tree)):
                if tree[i] in skill:
                    for j in range(list(skill).index(tree[i])):
                        if skill[j] in tree[i+1:] : return 0
                        if skill[j] not in tree[: i+1] : return 0 
            return 1
        cnt += isPosible(tree)
    return cnt