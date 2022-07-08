# programmers Lv2 124 나라의 숫자
# https://school.programmers.co.kr/learn/courses/30/lessons/12899

# 작성자 : 강동준
# 최초 작성일 : 2022-07-08
# 최종 작성일 : 

def divide(n, num):    
    standard_number = {1: '1', 2: '2', 3: '4'}
    if int(n/3) > 0:
        if( n <= 3):
            num.append(standard_number[n])
        else:
            k = divide(int(n/3), num)
            if( n % (3 * k) == 0):
                print("들")
                print(num)

                num.append(standard_number[3])
                print(num)
            else:
                num.append(standard_number[n%(3*k)])
            # print(n%(3*k), end ='')
            return int(n/3)
    elif int(n/3) == 0:
        num.append(standard_number[n])
        # print(n, end = '')
        return n

def solution(n):
    answer = ''
    k = []
    divide(n, k)
    answer = ''.join(s for s in k)
    return answer

n = 40
number = solution(n)
print(number)