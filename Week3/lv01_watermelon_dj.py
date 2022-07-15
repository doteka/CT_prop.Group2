# PROGRAMMERS Lv1 수박수박수박수박수박수?
# https://school.programmers.co.kr/learn/courses/30/lessons/12922

# 작성자 : 강동준
# 최초 작성일 : 2022-07-15
# 최종 작성일 : 2022-07-15

def solution(n):
    answer = ''
    last_char = ''

    if n%2 == 1:            # If it's odd, the last character is "수"
        last_char = "수"    # Initial value of last_char ""
    
    for index in range(0, int(n/2)):    # Since watermelon is 2 letters, repeat as much as you divide by 2
        answer += "수박"

    answer += last_char     # Add the last letter "수" or ""
    return answer

n = 5
answer = solution(n)
print(answer)