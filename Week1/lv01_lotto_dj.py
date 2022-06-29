# PROGRAMMERS LV01 로또의 최고 순위와 최저 순위
# https://programmers.co.kr/learn/courses/30/lessons/77484

# 작성자 : 강동준
# 최초 작성일 : 2022-06-29
# 최종 작성일 : 2022-06-29

def solution(lottos, win_nums):
    answer = []
    rank = [1, 2, 3, 4, 5, 6, 6]        # Ranking 
    count = 0                           # correct numbers
    unknownCount = 0                    # unknown numbers

    maxRank = 0
    maxRankIndex = 0

    minRank = 0
    minRankIndex = 0

    for value in lottos:
        if value in win_nums:           # If there is a correct number
            count += 1
            win_nums.remove(value)      # Remove correct number
        elif value == 0:                # If there is a unknown number
            unknownCount += 1

    if unknownCount <= len(win_nums):   # As many as unknown number All right Max Rank, All wrong Min Rank
        maxRankIndex = 6 - (count + unknownCount)
        minRankIndex = 6 - count

    else:                               # As many as win_number All right Max Rank, All wrong Min Rank
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