# PROGRAMMERS Lv1 음양 더하기
# https://school.programmers.co.kr/learn/courses/30/lessons/76501

# 작성자 : 강동준
# 최초 작성일 : 2022-07-29
# 최종 작성일 : 2022-07-29

def solution(absolutes, signs):
    answer = 0
    
    for i in range(len(signs)):
        if signs[i]:                        
            answer += absolutes[i]      # True is Plus
        else:
            answer -= absolutes[i]      # False is minus
            
    return answer

absolutes = [4,7,12]
signs = [True,False,True]
print(solution(absolutes, signs))