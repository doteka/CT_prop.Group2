# PROGRAMMERS LV2 기능 개발
# https://school.programmers.co.kr/learn/courses/30/lessons/42586

# 작성자 : 강동준
# 최초 작성일 : 2022-08-12
# 최종 작성일 : 20220-08-
def ceil(number):
    value = int(number)
    if value != number:     # Check for decimal points
        value += 1          # If there is, I will raise it
    return value

def solution(progresses, speeds):
    answer = []
    complet = []

    for index in range(len(progresses)):
        complet.append(ceil((100-progresses[index]) / speeds[index]))   # Calculating the number of remaining work days
    index = 0
    while(index < len(complet)):
        count = 0
        if(index+1 < len(complet) and complet[index] >= complet[index+1]):  # See if there are technologies that can be deployed together
            for i in range(index+1, len(complet)):
                if complet[index] >= complet[i]:
                    count += 1
                else:
                    break
        answer.append(count+1)
        index += (count + 1)

    return answer

progresses = [95, 90, 99, 99, 80, 99]	
speeds = [1, 1, 1, 1, 1, 1]	
print(solution(progresses, speeds))