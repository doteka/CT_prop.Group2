# PROGRAMMERS Lv2 [1차] 캐시
# https://school.programmers.co.kr/learn/courses/30/lessons/17680

# 작성자 : 강동준
# 최초 작성일 : 2022-08-05
# 최종 작성일 : 2022-08-08

CACHE_HIT = 1
CACHE_MISS = 5

def solution(cacheSize, cities):
    answer = 0
    cache = []
    if cacheSize == 0:                      # Page fault unconditionally occurs when cache size is 0
        return len(cities) * CACHE_MISS 

    for i in range(len(cities)):
        cities[i] = cities[i].upper()       # Change all to uppercase
        if cities[i] in cache:
            findIndex = cache.index(cities[i])  # See location with corresponding values
            del cache[findIndex]                # Remove values for that location
            answer += CACHE_HIT
        else:
            if len(cache) >= cacheSize:         # Remove the oldest used when there is no space in cache memory
                del cache[0]
            answer += CACHE_MISS
        cache.append(cities[i])
    return answer

# CACHE_HIT = 1
# CACHE_MISS = 5

# def solution(cacheSize, cities):
#     answer = 0
#     cache = []
#     pageIndex = 0
#     if cacheSize == 0:
#         return CACHE_MISS * len(cities)
        
#     for i in range(len(cities)):
#         cities[i] = cities[i].upper()
#         if cities[i] in cache:                  # cache hit
#             answer += CACHE_HIT
#             if pageIndex <= cache.index(cities[i]):
#                 pageIndex -= 1
#         else:                                   # cache miss
#             if len(cache) < cacheSize:          # cache not full
#                 cache.append(cities[i])
#             else:                               # cache full
#                 cache[pageIndex%cacheSize] = cities[i]      # page fault
            
#             answer += CACHE_MISS
#         pageIndex += 1                          # last using
#     return answer

cacheSize = 5
cities = ["A", "B", "A","C","D","E","A","F"]
print(solution(cacheSize, cities))