# PROGRAMMERS Lv2 [3차] 압축
# https://school.programmers.co.kr/learn/courses/30/lessons/17684

# 작성자 : 강동준
# 최초 작성일 : 2022-07-27
# 최종 작성일 : 2022-07-27

def solution(msg):
    answer = []
    word = {}
    last = 26
    for index in range(65, 91):
        word[chr(index)] = index - 64

    index = 0
    while(index < len(msg)):        # for문은 index를 키로 가질떄 index += 2가 불가능해서 while문 사용
        words = msg[index]
        count = 1
        for i in range(index, len(msg)): # 지금 문자를 기준으로 사전에 있는 제일 긴 단어 체크
            if (i < len(msg)-1):         # out of range 대비
                tmp = words + msg[i+1]
                if tmp in word:          # 현재의 문자가 사전에 있다면 계속 진행
                    count += 1
                    words = tmp
                else:
                    break
        keyword = ""
        for i in range(index, index + count):   # 기준 단어부터 제일 긴 단어까지 더해주기
            keyword += msg[i]
        answer.append(word[keyword])

        if index+count < len(msg):              # 이번에 체크한 단어와 그 다음 문자를 더한 새로운 단어를 사전에 저장
            key = keyword + msg[index+count]
            last += 1
            word[key] = last
        
        index += count

    return answer

msg = "KAKAO"                      # [11, 1, 27, 15]
msg1 = "TOBEORNOTTOBEORTOBEORNOT"  # [20, 15, 2, 5, 15, 18, 14, 15, 20, 27, 29, 31, 36, 30, 32, 34]
msg2 = "ABABABABABABABAB"          # [1, 2, 27, 29, 28, 31, 30]
print(solution(msg))
