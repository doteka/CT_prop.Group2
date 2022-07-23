# PROGRAMMERS Lv1 신규 아이디 추천
# https://school.programmers.co.kr/learn/courses/30/lessons/72410

# 작성자 : 강동준
# 최초 작성일 : 2022-07-22
# 최종 작성일 : 2022-07-

def step1(new_id):
    new_id = new_id.lower()
    return new_id
def step2(new_id):
    Allowed_Char = ['-', '_', '.']
    id = list(new_id)
    for index in range(0, len(new_id)):
        if id[index].isalpha():
            continue
        elif id[index].isdigit():
            continue
        elif id[index] in Allowed_Char:
            continue
        else:
            id[index] = ''
    new_id = ''.join(id)
    return new_id


def solution(new_id):
    answer = ''
    new_id = step1(new_id)
    new_id = step2(new_id)

    print(new_id)
    return answer

new_id = "...!@BaT#*..y.abcdefghijklm"
solution(new_id)