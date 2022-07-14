# PROGRAMMERS Lv2 스킬트리
# https://school.programmers.co.kr/learn/courses/30/lessons/49993#fn1

# 작성자 : 강동준
# 최초 작성일 : 2022-07-14
# 최종 작성일 : 2022-07-14


def solution(skill, skill_trees):
    answer = 0
    skill_Name = list(skill)
    check = []
    count = 0

    for i in range(0, len(skill_Name)):
        check.append(False)                 # False으로 배열 초기화
    
    for key in skill_trees:                 # 스킬트리 하나씩 추출 
        for index in key:                   # 스킬트리에서 각각의 스킬 이름을 추출
            if index in skill_Name:         # 추출한 스킬 이름이 선행 스킬에 있는지 확인하고 있으면 true
                check[skill_Name.index(index)] = True       
                if(check[0:skill_Name.index(index)].count(True) != len(check[0:skill_Name.index(index)])):  # 만약 지금 찍은 선행스킬의 선행스킬이 있는지 확인
                    break                   # 선행 스킬이 있는데 안찍었으면 loop 끝
                else:
                    count += 1              # 선행 스킬이 있는데 찍었으면 계속 loop
        if check[0:len(skill_Name)].count(True) == count:
            answer += 1
         
        for i in range(0, len(skill_Name)):
            check[i] = False                # 리스트 초기화
        count = 0                           # 배열 초기화


    return answer


skill = "CBDK"
skill_trees = ["CB", "CXYB", "BD", "AECD", "ABC", "AEX", "CDB", "CBKD", "IJCB", "LMDK"]
result = solution(skill, skill_trees)
print(result)


# 아래는 망한 코드

# def solution(skill, skill_trees):
#     answer = 0
#     skill_sequence = list(skill)
#     remove_set = {-1}
    
#     for skillName in skill_trees:
#         tempList = []
#         endToEnd = 0
#         endToEndLength = 0
#         for skill_SEQ in skill_sequence:
#             tempList.append(skillName.find(skill_SEQ))
#         noSkill = tempList.count(-1)
#         if noSkill == len(skill):
#             answer += 1
#         else:
#             skill_String = ''.join(map(str, tempList[0:len(tempList)-1]))
#             start = skill_String.find("-1")
#             end = skill_String.rfind("-1")                                # 선행 스킬을 찍지 않았을 경우
            
#             noNoSkill = tempList[start:end+1].count(-1)
#             noNoSkillLength = len(tempList[start:end])

#             if start != -1 and end != -1:
#                 endToEnd = tempList[end: len(tempList)].count(-1)
#                 endToEndLength = len(tempList[end: len(tempList)])

#             # tempList = [i for i in tempList if i not in remove_set]
#             tempTwoList = tempList[:]
#             tempTwoList.sort()

#             if(noNoSkill == noNoSkillLength and tempList == tempTwoList and endToEnd == endToEndLength):
#                 answer += 1
#                 print(tempList)
        
#         # print(tempList)
#     # print(skill_sequence)

#     return answer


# skill = "CBD"
# skill_trees = ["BACDE", "CBADF", "AECB", "BDA"]
# result = solution(skill, skill_trees)
# print(result)