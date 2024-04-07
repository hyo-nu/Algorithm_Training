

def solution(players, callings):
    players_dict = { name : idx for idx, name in enumerate(players)}
    for call in callings:
        front = players[players_dict[call]-1]
        players_dict[front] += 1
        players_dict[call] -= 1
        
        players[players_dict[front]], players[players_dict[call]] =  players[players_dict[call]], players[players_dict[front]]
    return players