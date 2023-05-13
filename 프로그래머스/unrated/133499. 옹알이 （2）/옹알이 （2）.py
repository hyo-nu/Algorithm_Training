# aya, ye, woo, ma

def solution(babbling):
    talk = ['aya','ye','woo','ma']
    talk_check = []
    
    for ba in babbling:
        tmp = ba
        for i in range(len(talk)):
            tmp = tmp.replace(talk[i],str(i))
        talk_check.append(tmp)
    
    word_cnt = 0
    for word in talk_check:
        if not word.isdigit() : continue
        else:
            for i in range(len(word)-1):
                if word[i]==word[i+1]:
                    break
            else:word_cnt += 1
    
    return word_cnt