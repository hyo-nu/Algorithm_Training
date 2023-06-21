from itertools import permutations

def solution(k, dungeons):
    tour_max = 0
    for arr in permutations(dungeons,len(dungeons)):
        tired, tour = k, 0
        for lst in arr:
            if tired < lst[0] : break
            tired -= lst[1]
            tour += 1
        tour_max = max(tour_max,tour)
    return tour_max