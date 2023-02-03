def solution(polynomial):
    hang = polynomial.split(' + ')
    hang_x = []
    hang_num_sum = 0

    for h in hang:
        if str(h[len(h)-1]) == 'x':
            if len(h) != 1:
                hang_x.append(int(h.replace('x','')))
            else:
                hang_x.append(int(h.replace('x','1')))
        else:
            hang_num_sum += int(h)
    
    
    if sum(hang_x) > 1 and hang_num_sum > 0:
        return f'{sum(hang_x)}x + {hang_num_sum}'
    
    elif sum(hang_x) > 1 and hang_num_sum == 0:
        return f'{sum(hang_x)}x'
    
    elif sum(hang_x) == 1 and hang_num_sum > 0:
        return f'x + {hang_num_sum}'
    
    elif sum(hang_x) == 1 and hang_num_sum == 0:
        return f'x'
    
    elif sum(hang_x) == 0 and hang_num_sum > 0:
        return f'{hang_num_sum}'
    
    elif sum(hang_x) == 0 and hang_num_sum == 0:
        return