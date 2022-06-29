# PROGRAMMERS LV01 로또의 최고 순위와 최저 순위
# https://programmers.co.kr/learn/courses/30/lessons/77484

# 작성자 : 강동준
# 최초 작성일 : 2022-06-29
# 최종 작성일 : 2022-06-29

def solution(lottos, win_nums):
    answer = []
    rank = [1, 2, 3, 4, 5, 6, 6]        # 순위를 배열화. 후반에 6 - count 식으로 해줄 예정
    count = 0                           # 맞춘 숫자 갯수
    unknownCount = 0                    # 알아보지 못하는 수

    maxRank = 0
    maxRankIndex = 0

    minRank = 0
    minRankIndex = 0

    for value in lottos:
        if value in win_nums:           # 맞춘 숫자가 있을 경우
            count += 1
            win_nums.remove(value)      # 맞춘 숫자는 list에서 제거
        elif value == 0:                # 알아보지 못하는 수 인 경우.
            unknownCount += 1

    if unknownCount <= len(win_nums):   # 알아보지 못하는 수가 당첨 수의 갯수보다 작은 경우에는 다 맞추면 최고 순위, 다 못맞추면 최저 순위
        maxRankIndex = 6 - (count + unknownCount)
        minRankIndex = 6 - count

    else:                               # 알아보지 못하는 수가 당첨 수의 갯수보다 큰 경우에는 당첨 수의 갯수만큼 다 맞추면 최고 순위, 다 못맞추면 최저 순위
        maxRankIndex = 6 - (count + len(win_nums))
        minRankIndex = 6 - count

    maxRank = rank[maxRankIndex]
    minRank = rank[minRankIndex]

    answer.append(maxRank)
    answer.append(minRank)

    return answer

lottos = [45, 4, 35, 20, 3, 9]
win_nums = [20, 9, 3, 45, 4, 35]
answer = solution(lottos, win_nums)
print(answer)

# for i in range(0, 6):
#     arr[i] = int(input().split(','))

# for i in range(0, 6):
#     print(arr[i], end=' ')