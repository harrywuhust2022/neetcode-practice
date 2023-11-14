class Solution:
    def solveNQueens(self, n: int):
        res = []
        
        cols = set()
        posDiag = set()                           # row + col == constant 
        negDiag = set()                           # row - col == constant

        board = [["."] * n for i in range(n) ]    # board 是 不断更新的，类似 tmp = []

        def backtrack(r):
            if r == n:
                copy = ["".join(row) for row in board]
                res.append(copy)
                return
            
            for c in range(n):
                if c in cols or (r+c) in posDiag or (r-c) in negDiag:
                    continue

                # backtrack template
                cols.add(c)
                posDiag.add(r+c)
                negDiag.add(r-c)
                board[r][c] = "Q"

                backtrack(r+1)
                
                cols.remove(c)
                posDiag.remove(r+c)
                negDiag.remove(r-c)
                board[r][c] = "."

        backtrack(0)
        return res


Nqueens = Solution()
print(Nqueens.solveNQueens(n=4))


'''
同一水平线/垂直线/两条对角线上只能有一个 Q, 其余用"."替代

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        cols = set()
        posDiag = set()             # (r + c) == a fix number
        negDiag = set()             # (r - c) == a fix number
        board = [["."] * n for i in range(n)]

        def backtrack(r):           # 以行数作为 index
            if r == n:              # 如果到了最后一行，更新res
                copy = ["".join(row) for row in board]
                res.append(copy)
                return
            for c in range(n):
                if (c in cols) or ((r + c) in posDiag) or ((r - c) in negDiag):
                    continue        # 棋盘规则，同一水平线/垂直线/两条对角线 上 不能有2个Q 
                
                cols.add(c)
                posDiag.add(r + c)
                negDiag.add(r - c)
                board[r][c] = "Q"   # backtrack模板：先更新棋盘

                backtrack(r + 1)    # 递归
                
                cols.remove(c)
                posDiag.remove(r + c)
                negDiag.remove(r - c)
                board[r][c] = "."   # 把棋盘恢复
        backtrack(0)
        return res

'''