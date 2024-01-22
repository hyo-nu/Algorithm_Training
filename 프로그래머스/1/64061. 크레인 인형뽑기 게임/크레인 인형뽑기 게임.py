# 5 <= 배열의 크기 <= 30
# 1 <= 인형번호 <= 100
# 1 <= 뽑기 <= 1000


def solution(board, moves):
    board = list(map(list,zip(*board[::-1])))
    basket = []
    bomb = 0
    
    for spot in moves:
        while True:
            if not board[spot-1] : break
            doll = board[spot-1].pop()
            if doll : basket.append(doll) ; break
        
        if len(basket) >= 2 and basket[-1] == basket[-2]:
            basket.pop()
            basket.pop()
            bomb += 2
    
    return bomb