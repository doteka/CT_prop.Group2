# programmers Lv2 124 나라의 숫자
# https://school.programmers.co.kr/learn/courses/30/lessons/12899

# 작성자 : 강동준
# 최초 작성일 : 2022-07-08
# 최종 작성일 : 

def divide(n, num):    
    standard_number = {1: '1', 2: '2', 3: '4'}
    if int(n/4) > 0:
        if( n <= 4):
            num.append(standard_number[n%4])
        else:
            k = divide(int(n/4), num)
            # print("C ", n%3, n)
            if( n % (4) == 0):
                num.append(standard_number[3])
                # print(num)
            else:
                num.append(standard_number[n%(4)])
            # print(n%(3*k), end ='')
            return int(n/4)
    elif int(n/4) == 0:
        num.append(standard_number[n%4])
        # print(n, end = '')
        return n

def solution(n):
    answer = ''
    k = []
    divide(n, k)
    answer = ''.join(s for s in k)
    return answer

n = 4
number = solution(n)
print(number)