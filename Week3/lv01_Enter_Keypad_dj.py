# PROGRAMMERS Lv1 [카카오 인턴] 키패드 누르기
# https://school.programmers.co.kr/learn/courses/30/lessons/67256

# 작성자 : 강동준
# 최초 작성일 : 2022-07-17
# 최종 작성일 : 2022-07-17

def findPosition(keyPad, number):                   # find position in number Keypad 
    x = y = 0
    for index in range(len(keyPad)):
        if str(number) in keyPad[index]:
            x = index                               # position X
            y = keyPad[index].index(str(number))    # postion Y
            break
    return x, y

def click(answer, clickHand, prev, nextNumber):     # Number Click
    if clickHand == 'L':
        index = 0
    else:
        index = 1
    answer += clickHand
    prev[index] = nextNumber                        # index 0 = Left Hand, index 1= Right Hand
    return answer, prev
    
def solution(numbers, hand):
    answer = ''
    numbers = list(numbers)
    keyPad = [['1', '2', '3'], ['4', '5', '6'], ['7', '8' ,'9'] , ['*', '0', '#']]
    leftNumber = ['1', '4', '7']
    rightNumber = ['3', '6', '9']
    clickHand = ''
    prev = ['*', '#']
    
    for nextNumber in numbers:
        if str(nextNumber) in leftNumber:               # Left Line Numbers
            clickHand = 'L'
        elif str(nextNumber) in rightNumber:            # Right Line Numbers
            clickHand = 'R'
        else:
            leftX, leftY = findPosition(keyPad, prev[0])     # Find the current position of the left hand   
            rightX, rightY = findPosition(keyPad, prev[1])   # Find the current position of the right hand
            nextX, nextY = findPosition(keyPad, nextNumber)  # Find a numeric position
            
            leftDiff = abs(abs(leftX - nextX) + abs(leftY - nextY))    # Calculate the next position difference from the previous left position
            rightDiff = abs(abs(rightX - nextX) + abs(rightY - nextY)) # Calculate the next position difference from the previous right position


            if leftDiff == rightDiff:                       # If the difference is the same
                if hand == "left":                          # Priority Comparison
                    clickHand = 'L'
                else:
                    clickHand = 'R' 
            elif leftDiff < rightDiff:
                clickHand = 'L'
            else:
                clickHand = 'R'
        answer, prev = click(answer, clickHand, prev, nextNumber)
    return answer

numbers = [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]
hand = "right"
print(solution(numbers, hand))