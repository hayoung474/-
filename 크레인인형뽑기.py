def solution(board, moves):
    basket = []
    answer = 0
    for move in moves:
        for row in range(len(board[move-1])):
            if(board[row][move-1] != 0):
                print(board[row][move-1])
                
                if(len(basket)!= 0):
                    if(basket[-1] != board[row][move-1]):
                        basket.append(board[row][move-1])
                    else:
                        basket.pop()
                        answer +=2
                else:
                    basket.append(board[row][move-1])
                board[row][move-1]=0
                break
    return answer
board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
moves = [1,5,3,5,1,2,1,4]
print(solution(board, moves))