# PROGRAMMERS Lv1 소수 만들기
# https://school.programmers.co.kr/learn/courses/30/lessons/12977

# 작성자 : 강동준
# 최초 작성일 : 2022-08-02
# 최종 작성일 : 2022-08-02

from itertools import *

def solution(nums):
    answer = 0

    numberList = list(combinations(nums, 3))        # (nums)C(3)

    for key in numberList :
        value = sum(key)                            # Sum
        check = False                               # Decide if it's a prime number
      
        for i in range(2, value):                   # 2 ~ value - 1
            if value % i == 0:
                check = True                        # If you have mineral water, it's not a small number because you've excluded yourself from Lesson 1
                break
        
        if check == False:
            answer += 1
        
    
    return answer

# nums = [1, 2, 3, 4]
nums = [1, 2, 7, 6, 4]
print(solution(nums))