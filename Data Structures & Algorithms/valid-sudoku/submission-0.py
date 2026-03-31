class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowCheck=set()
        colCheck=set()
        squareCheck={}

        i,j=0,0
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j]==".":
                    continue
                if board[i][j] in rowCheck:
                    return False
                else:
                    rowCheck.add(board[i][j])
            rowCheck=set()

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[j][i]==".":
                    continue
                if board[j][i] in colCheck:
                    return False
                else:
                    colCheck.add(board[j][i])
            colCheck=set()

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j]==".":
                    continue
                if (i//3,j//3) in squareCheck:
                    if board[i][j] in squareCheck[(i//3,j//3)]:
                        return False
                    else:
                        squareCheck[(i//3,j//3)].add(board[i][j])
                else:
                    squareCheck[(i//3,j//3)]=set()
                    squareCheck[(i//3,j//3)].add(board[i][j])
        return True

        