def solution(book_time):
    reserve = []
    min_sp = 1500
    max_ep = 0
    for book in book_time:
        st, et = book[0].split(":"),book[1].split(":")
        sp, ep = (int(st[0]) * 60 + int(st[1])), (int(et[0]) * 60 + int(et[1]) + 10)
        reserve.append((sp,ep))
        min_sp = min(min_sp, sp)
        max_ep = max(max_ep, ep)
    
    times = [0] * (max_ep - min_sp + 1)
    for sp, ep in reserve:
        for i in range(sp, ep):
            times[i-min_sp] += 1
        
    return max(times)