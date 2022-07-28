# PROGRAMMERS Lv1 다트 게임
# https://school.programmers.co.kr/learn/courses/30/lessons/17682

# 작성자 : 강동준
# 최초 작성일 : 2022-07-28
# 최종 작성일 : 2022-07-28

def solution(dartResult):
    answer = 0
    Result = []
    modifier = {'S':1, 'D':2, 'T': 3}
    index = 0
    optionRun = False
    number = ""
    for i in dartResult:
        if optionRun:
            if i == "*":
                if index == 0:              # When index is zero, only the first value is doubled
                    Result[index] *= 2
                else:                       # If index is not zero, double the previous and current values are doubled
                    Result[index] *= 2  
                    Result[index-1] *= 2
            elif i == "#":
                Result[index] *= -1         # Current value minus
            else:
                optionRun = False           # variable init
                number = ""
                index +=1 
        if i.isdigit():
            number += i                     # Obtain a number consisting of characters
        elif i.isalpha():
            Result.append(int(number) ** modifier[i]) # Add bonus points
            optionRun = True
    answer = sum(Result)
        
    return answer

dartResult = "1D2S3T*"
print(solution(dartResult))