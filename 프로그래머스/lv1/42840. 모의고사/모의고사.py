def solution(answers):
    one = [1,2,3,4,5] * (len(answers)//5 + 1)
    two = [2,1,2,3,2,4,2,5] * (len(answers)//8 + 1)
    three = [3,3,1,1,2,2,4,4,5,5] * (len(answers)//10 + 1)

    score1 = score2 = score3 = 0
    for i in range(len(answers)):
        if one[i] == answers[i]: score1 += 1
        if two[i] == answers[i]: score2 += 1
        if three[i] == answers[i]: score3 += 1
    
    scores = [score1,score2,score3]
    win = max(scores)
    winner = []
    for idx, score in enumerate(scores,1):
        if score == win:
            winner.append(idx)

    return winner