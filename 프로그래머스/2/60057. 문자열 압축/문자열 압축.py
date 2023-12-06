def solution(s):
    s_len = len(s)
    Min = s_len
    for cut in range(1,s_len // 2 + 1):
        compressed = ""
        prev_str = s[0 : cut]
        count = 1
        for i in range(cut,s_len,cut):
            if prev_str == s[i : i + cut]:
                count += 1
            else: 
                compressed += str(count) + prev_str if count >= 2 else prev_str
                prev_str = s[i : i + cut]
                count = 1
                
        compressed += str(count) + prev_str if count >= 2 else prev_str
        Min = min(Min,len(compressed))
        
    return Min