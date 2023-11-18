class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])

        def dfs(r, c):
            if r in range(ROWS) and c in range(COLS) and board[r][c] == "O":
                board[r][c] = "T"
                dfs(r-1, c)
                dfs(r+1, c)
                dfs(r, c-1)
                dfs(r, c+1)
            else:
                return
        
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O" and (r in [0, ROWS-1] or c in [0, COLS-1]):
                    dfs(r, c)
        
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O":
                    board[r][c] = "X"
        
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "T":
                    board[r][c] = "O"

'''

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows, cols = len(board), len(board[0])

        def dfs(r, c):
            if r in range(rows) and c in range(cols) and board[r][c] == "O":
                board[r][c] = "T"
                dfs(r+1, c)
                dfs(r-1, c)
                dfs(r, c+1)
                dfs(r, c-1)
            else:
                return
        
        # 1. (DFS) 将所有与边界上连通的"O"都筛选出来 ("O" -> "T")
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O" and (r in [0, rows-1] or c in [0, cols-1]):
                    dfs(r, c)
        
        # 2. 把棋盘中间的所有"O"变成 X ("O" -> "X")
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O":
                    board[r][c] = "X"
        
        # 3. 把边界和连通的变成 O ("T" -> "O")
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "T":
                    board[r][c] = "O"

# 题意：把棋盘中所有被 X 包围的 O 都变成 X。秘诀：棋盘边界上所有连通的O都要求保留
# 所以我们需要用 dfs 找出所有与边界的 "O" 连通的部分，把他们先变成T，然后最后恢复。

# Time: O(n*m) 棋盘大小

'''