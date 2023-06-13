def merge(sr,sc,er,ec,R,C,cnt):
    global result
    if sr == er and sc == ec:
        result = cnt
        return

    R_mid = (sr + er) // 2
    C_mid = (sc + ec) // 2
    if sr <= R <= R_mid and sc <= C <=C_mid: # 위 왼쪽
        merge(sr,sc,R_mid,C_mid,R,C,cnt)
    elif sr <= R <= R_mid and C_mid+1 <= C <= ec:
        merge(sr,C_mid+1,R_mid,ec,R,C,cnt + ((R_mid-sr+1)*(ec-C_mid))) # 위 오른쪽
    elif R_mid+1 <= R <= er and sc <= C <= C_mid:
        merge(R_mid+1,sc,er,C_mid,R,C,cnt + ((er-R_mid)*(C_mid-sc+1)*2)) # 아래 왼쪽
    elif R_mid+1 <= R <= er and C_mid+1 <= C <= ec:
        merge(R_mid+1,C_mid+1,er,ec,R,C,cnt + ((er-R_mid)*(ec-C_mid)*3)) # 아래 오른쪽

N, R, C = map(int,input().split())
merge(0,0,2**N-1,2**N-1,R,C,0)
print(result)