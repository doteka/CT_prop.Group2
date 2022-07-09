# programmers Lv1 문자열 다루기 기본
# https://school.programmers.co.kr/learn/courses/30/lessons/12918

# 작성자 : 강동준
# 최초 작성일 : 2022-07-09
# 최종 작성일 : 2022-07-09


def solution(s):
    answer = True
    count = 0
    length = len(s)                     # string length

    if(length == 4 or length == 6):     # length 4 to 6 distinction
        for i in range(0, length):
            if s[i].isdigit():          # distinction if it's a number 
                count += 1

        if(count == length):            # If it's the same True Or False
            answer = True
        else:
            answer = False
    else:                               # length out of range
        answer = False        
    return answer

a = "a234"
print(solution(a))