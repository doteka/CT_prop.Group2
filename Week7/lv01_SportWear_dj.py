# PROGRAMMERS LV1 체육복
# https://school.programmers.co.kr/learn/courses/30/lessons/42862

# 작성자 : 강동준
# 최초 작성일 : 2022-08-12
# 최종 작성일 : 20220-08-12

def solution(n, lost, reserve):
    answer = 0
    reserve_DICT = {}

    lost.sort()
    print(lost)

    for key in reserve:
        if key in lost:                 # in case of theft
            index = lost.index(key)     # a personal use of extra gym clothes
            del lost[index]
        else:
            reserve_DICT[key] = 1       # a student with extra clothes, Change to dictionary for easier access

    answer += n - len(lost)             # a student who can take classes

    for i in lost:
        if reserve_DICT.get(i-1, 0) == 1:   # The priority is to check if there is a student with the previous number
            answer += 1
            reserve_DICT[i-1] = 0
        elif reserve_DICT.get(i+1, 0) == 1: # You can give the back number to another student
            answer += 1
            reserve_DICT[i+1] = 0
        
    return answer

n = 5
lost = [1, 2, 4]
reserve = [2, 3, 4, 5]
print(solution(n, lost, reserve))