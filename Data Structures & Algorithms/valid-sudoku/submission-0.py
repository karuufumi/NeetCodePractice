class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        sqr = set()
        for i in range(len(board)):
            row = set()
            col = set()
            for j in range(len(board)):
                if board[i][j] != '.':
                    if board[i][j] in row: return False
                    row.add(board[i][j])
                if board[j][i] != '.':
                    if board[j][i] in col: return False
                    col.add(board[j][i])
                x=int(j/3)+int(i/3)*3
                y=(int(j%3)+3*i)%9

                square = board[x][y]
                if x%3==0 and y%3==0:
                    sqr = set()

                if square != '.':
                    if square in sqr:
                        return False
                    sqr.add(square)
        return True
