# PROGRAMMERS Lv1 신규 아이디 추천
# https://school.programmers.co.kr/learn/courses/30/lessons/72410

# 작성자 : 강동준
# 최초 작성일 : 2022-07-22
# 최종 작성일 : 2022-07-23

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
def step3(new_id):
    id = ''
    count = 0
    index = 0
    while index < len(new_id):
        if new_id[index] != ".":
            id += new_id[index]
            index += 1
        else:
            count = 1
            while True:
                if(index + count >= len(new_id)):
                    break
                if new_id[index + count] == '.':
                    count += 1
                else:
                    break
            id += '.'
            index += count

    return id
def step4(new_id):
    start = 0
    end = len(new_id)
    if new_id[start] == '.':
        start = 1
    if new_id[end-1] == '.':
        end = len(new_id)-1
    return new_id[start:end]
def step5(new_id):
    if new_id == "":
        new_id = "a"

    return new_id
def step6(new_id):
    if len(new_id) >= 16:
        new_id = new_id[0:15]
        new_id = step4(new_id)
    
    return new_id
def step7(new_id):
    if len(new_id) <= 2:
        last = new_id[len(new_id)-1]
        while len(new_id) < 3:
            new_id += last
    return new_id

def solution(new_id):
    answer = ''
    new_id = step1(new_id)
    new_id = step2(new_id)
    new_id = step3(new_id)
    new_id = step4(new_id)
    new_id = step5(new_id)
    new_id = step6(new_id)
    new_id = step7(new_id)
    return new_id