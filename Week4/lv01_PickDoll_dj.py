# PROGRAMMERS Lv1 크레인 인형뽑기 게임
# https://school.programmers.co.kr/learn/courses/30/lessons/64061

# 작성자 : 강동준
# 최초 작성일 : 2022-07-21
# 최종 작성일 : 2022-07-21

def solution(board, moves):
    answer = 0
    stack = []

    for key in moves:
        for index in range(0, len(board)):
            if board[index][key-1] != 0:            # Checking for dolls
                if len(stack) != 0 and (stack[len(stack)-1] == board[index][key-1]):    # len != 0 is list index out of range Prevention, Compare the last doll you picked with the doll
                    answer += 2
                    stack.pop()                     # list last data pop
                else:
                    stack.append(board[index][key-1])

                board[index][key-1] = 0             # Remove the doll
                break

    return answer

board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
moves = [1,5,3,5,1,2,1,4]
print(solution(board, moves))