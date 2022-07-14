# programmers Lv2 가장 큰 수
# https://school.programmers.co.kr/learn/courses/30/lessons/42746

# 작성자 : 강동준
# 최초 작성일 : 2022-07-10
# 최종 작성일 : 

import math

def solution(numbers):
    answer = ''
    a1 = ''
    a2 = ''
    dic = {}
    l = []
    word = ['a','b','c','d','e','f','g']
    word.reverse()
    for i in numbers:
        number_Length = len(str(i))
        tmp = str(i / (10 ** (number_Length-1))) + str(word[number_Length-1])
        # print(tmp)
        dic[tmp] = i
        l.append(tmp)
    l.sort(reverse=True)
    for i in l:
        a1 += str(dic[i])
    l.sort(reverse=False)
    for i in l:
        a2 += str(dic[i])

    if a1 > a2:
        answer = a1
    else:
        answer = a2
    
    if int(answer) == 0:
        answer = '0'
    return answer

numbers = [101, 10]	
answer = solution(numbers)
print(answer)