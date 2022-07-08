# programmers Lv1 숫자 문자열과 영단어
# https://school.programmers.co.kr/learn/courses/30/lessons/81301

# 작성자 : 강동준
# 최초 작성일 : 2022-07-08
# 최종 작성일 : 2022-07-08


def solution(s):
    answer = 0
    word = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"] # Word Array

    for index in range(0, len(word)):
        s = s.replace(word[index], str(index))      # word transform to number and repalce(str, str) so index integer to string
    answer = int(s)                         # string to integer
    return answer

s = "one4seveneight"
a = solution(s)
print(a)