import numpy as np

def pickDolls(board, moves):
    L = len(board)
    # print(L) #5
    arrBoard = np.array(board)
    # print(arrBoard)
    # print(arrBoard[0, 3], arrBoard[2, 2]) # 0 5

    result = []
    count = 0
    for move in moves:
        # print('--------', move, '---------')
        for i in range(L):
            if arrBoard[i, move-1] != 0:
                result.append(arrBoard[i, move-1])
                arrBoard[i, move-1] = 0
                # print('test1', result)
                break
            # print('test2')
        lengthResult = len(result)
# 런타임 에러
# 0 0 0 0
# 0 0 1 0
# 0 2 4 1
# 0 3 2 4
# 처음부터 한 줄 전체 인형 없을 때 top1 값때문에 컴파일에러

        top1, top2 = 0, 0
        if lengthResult >= 1:
            top1 = result[lengthResult-1]
        if lengthResult >= 2:
            top2 = result[lengthResult-2]
        # print(top1, top2)
        if top1 and top1 == top2:
            count += 2
            result = result[0:lengthResult-2]
        # print('test3 : ', result)
        
    return count

# board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[0,2,4,4,2],[0,5,1,3,1]]
moves = [1,5,3,5,1,2,1,4]

print(pickDolls(board, moves))