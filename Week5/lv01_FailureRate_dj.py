# PROGRAMMERS Lv1 실패율
# https://school.programmers.co.kr/learn/courses/30/lessons/42889

# 작성자 : 강동준
# 최초 작성일 : 2022-07-28
# 최종 작성일 : 2022-07-28

def solution(N, stages):
    answer = []
    dic = {}
    Fail = {}
    total = 0
    Fail_Stage = []
    Fail_Fails = []
    for index in range(1, N+2):
        dic[index] = stages.count(index)        # Check the number of people who passed the stage
        
    for index in range(N+1, 0, -1):
        if index == N+1:
            total += dic[index]
        else:
            total += dic[index]
            if total != 0:
                Fail[index] = dic[index] / total    # Calculating the Failure Rate
            else:
                Fail[index] = 0

    for index in range(1, N+1):
        if index == 1:                              # Add the first data that is the baseline
            Fail_Stage.append(index)
            Fail_Fails.append(Fail[index])
        else:
            check = False
            for i in range(0, len(Fail_Fails)):
                if Fail[index] > Fail_Fails[i]:     # Add data with high failure rates to the front
                    Fail_Stage.insert(i, index)
                    Fail_Fails.insert(i, Fail[index])
                    check = True
                    break
                else:
                    check = False
            if check == False:                      # Add low-failure data to the end
                Fail_Stage.append(index)
                Fail_Fails.append(Fail[index])

    answer = Fail_Stage
    return answer

N = 5
stages = [3,3,3,3]
print(solution(N, stages))