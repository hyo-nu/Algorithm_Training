def solution(players, callings):
    players_dict = { name : idx for idx, name in enumerate(players)}
    for before_name in callings:
        before_order = players_dict[before_name]
        players_dict[before_name] -= 1
        players_dict[players[before_order - 1]] += 1
        
        players[before_order-1], players[before_order] =  players[before_order], players[before_order-1]
        
    return players