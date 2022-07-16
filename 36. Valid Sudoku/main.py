def isValidSudoku(board: list[list[str]]) -> bool:
    for i in range(9):
        temp = []
        for j in range(9):
            if board[i][j] == '.':
                continue
            elif board[i][j] in temp:
                return False
            else:
                temp.append(board[i][j])

    for i in range(9):
        temp = []
        for j in range(9):
            if board[j][i] == '.':
                continue
            elif board[j][i] in temp:
                return False
            else:
                temp.append(board[j][i])

    for i in range(0, 9, 3):
        temp = []
        for j in range(i, i + 3):
            if board[i][j] == '.':
                continue
            elif board[i][j] in temp:
                return False
            else:
                temp.append(board[i][j])

    return True


board = [[".", ".", ".", ".", "5", ".", ".", "1", "."],
         [".", "4", ".", "3", ".", ".", ".", ".", "."],
         [".", ".", ".", ".", ".", "3", ".", ".", "1"],
         ["8", ".", ".", ".", ".", ".", ".", "2", "."],
         [".", ".", "2", ".", "7", ".", ".", ".", "."],
         [".", "1", "5", ".", ".", ".", ".", ".", "."],
         [".", ".", ".", ".", ".", "2", ".", ".", "."],
         [".", "2", ".", "9", ".", ".", ".", ".", "."],
         [".", ".", "4", ".", ".", ".", ".", ".", "."]]

print(isValidSudoku(board))
