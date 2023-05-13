# 100글자 이내로
# 영문 대소문자, 숫자, 공백, 마침표, 빼기
# 영문자로 시작 and 숫자 하나 이상 포함
# HEAD : 문자로만, 한글자이상
# NUMBER : 0< <99999
# TAIL : 숫자 다시 생성가능, 아무것도 없을수도



def solution(files):
    def Str(x):
        for i in range(len(x)):
            if x[i].isdigit():
                return i 
    def Num(i,x):
        for j in range(i,len(x)):
            if not x[j].isdigit():
                return j
            
    # files.sort(key = lambda x : ( x[:Str(x)].lower(),len(str(int(x[Str(x):Num(Str(x),x)]))), x[Str(x):Num(Str(x),x)]))
    files.sort(key = lambda x : ( x[:Str(x)].lower(),int(x[Str(x):Num(Str(x),x)])))   
    

    return files