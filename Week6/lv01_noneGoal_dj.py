# PROGRAMMERS Lv1 완주하지 못한 선수
# https://school.programmers.co.kr/learn/courses/30/lessons/42576

# 작성자 : 강동준
# 최초 작성일 : 2022-08-09
# 최종 작성일 : 2022-08-09

def solution(participant, completion):
    answer = ''
    dict = {}
    for key in participant:
        data = dict.get(key, 0)     # Returns a value corresponding to a key if it exists and a value corresponding to 0 if it does not exist
        dict[key] = data + 1        # Personnel

    for key in completion:
        if (dict[key] == 1):        # If there is only one person, it will be zero, so delete it
            del dict[key]           # To convert to a list later
        else:                       # If there are more than one, take one out
            dict[key] = dict[key] - 1
    answer = list(dict)[0]          # If it's 0, we deleted all of them, so the names of the people who are left in room 0 unconditionally

    return answer

participant = ["marina", "josipa", "nikola", "vinko", "filipa"]
completion = ["josipa", "filipa", "marina", "nikola"]
print(solution(participant, completion))