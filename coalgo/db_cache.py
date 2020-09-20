def solution(cacheSize, cities):
    from collections import OrderedDict
    cache = OrderedDict()
    elapsed = 0
    for city in cities:
        city = city.lower()
        if cache.get(city):
            # hit
            elapsed += 1
            cache.pop(city)
        else:
            # miss
            if len(cache) >= cacheSize:
                LRU(cache)
            elapsed += 5
        # 3rd err
        if len(cache) < cacheSize:
            cache[city] = True
            
    return elapsed

# 2nd err
def LRU(cache):
    if not cache:
        return
    cache.popitem(0)
