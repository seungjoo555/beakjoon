def solution(board, moves):
    stack = []
    answer = 0
    for i in moves:
        for j in range(len(board)):
            check = board[j][i-1]
            if check:
                if stack and stack[-1] == check:
                    stack.pop()
                    answer += 2
                else:
                    stack.append(check)
                board[j][i-1] = 0
                break
    return answer