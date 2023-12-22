def solution(cacheSize, cities):
    time = 0
    cache = []
    
    for city in cities:
        city = city.lower()
        if city in cache:
            cache.remove(city)
            cache.append(city)
            time += 1
        
        else:
            if len(cache) < cacheSize:
                cache.append(city)
            elif len(cache) == cacheSize:
                cache.append(city)
                cache.pop(0)
            time += 5
    
    return time