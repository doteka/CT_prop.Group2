def solution(nums):
    ABLE_TO_HAVE = int(len(nums) / 2)   # 가질 수 있는 최대 수
    answer = 0
    type = {}
    
    for monster in nums:
        type[monster] = 0               # 딕셔너리 초기화
    
    for monster in nums:
        type[monster] += 1              # 각 타입에 해당하는 폰켓몬 수 체크
    
    if len(type) >= ABLE_TO_HAVE:       # 폰켓몬의 종류보다 가질 수 있는 수가 크면, 가질 수 있는 종의 최대 값은 가질 수 있는 수
        answer = ABLE_TO_HAVE
    else:                               # 폰켓몬의 종류가 가질 수 있는 수보다 작으면, 폰켓몬의 종류가 가질 수 있는 종의 최댓값
        answer = len(type)
    
    return answer


nums = [3,3,3,2,2,2]
result = solution(nums)
print(result)