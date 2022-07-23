# PROGRAMMERS Lv1 콜라츠 추측
# https://school.programmers.co.kr/learn/courses/30/lessons/12943

# 작성자 : 강동준
# 최초 작성일 : 2022-07-22
# 최종 작성일 : 2022-07-22


def solution(num):
    answer = 0
    while True:
        if num == 1:
            break
        elif answer >= 500:
            answer = -1
            break
        else:
            if num % 2 == 1:
                num = num * 3 + 1
            else:
                num /= 2
            answer += 1
    return answer


num = 6
print(solution(num))