# PROGRAMMERS Lv1 [1차] 비밀지도
# https://school.programmers.co.kr/learn/courses/30/lessons/17681

# 작성자 : 강동준
# 최초 작성일 : 2022-07-15
# 최종 작성일 : 2022-07-15

def diveList(maxLength, array, map):
    for key in array:
        dive = list(format(key, 'b'))       # List by changing decimal to binary
        map.append(dive)
        if maxLength < len(dive):           # Find the maximum length
            maxLength = len(dive)
    return maxLength, map

def addZero(maxLength, map):
    len_temp = 0 
    for key in map:
        if maxLength > len(key):                        # If the current length is less than the maximum length
            len_temp = len(key)
            for i in range(0, maxLength-len_temp):      # Decide that the first zero is omitted
                key.insert(i, 0)
    return map

def solution(n, arr1, arr2):
    answer = []
    map1 = []
    map2 = []
    maxLength = 0

    maxLength, map1 = diveList(maxLength, arr1, map1)
    maxLength, map2 = diveList(maxLength, arr2, map2)
    map1 = addZero(maxLength, map1)
    map2 = addZero(maxLength, map2)

    for indexX in range(0, len(map1)):
        answer.append("")
        for indexY in range(0, maxLength):
            if int(map1[indexX][indexY]) or int(map2[indexX][indexY]):      # Use the point where the number 0 is False and 1 is True
                answer[indexX] += "#"
            else:
                answer[indexX] += " "
    
    return answer

n = 5
arr1 = [9, 20, 28, 18, 11]
arr2 = [30, 1, 21, 17, 28]
answer = solution(n, arr1, arr2)
print(answer)