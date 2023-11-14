class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        path = set()

        def dfs(r, c, i):            # row, col, index i of word, word[i]
            if i == len(word):
                return True          # successfully find it.
            
            if (r not in range(ROWS) or c not in range(COLS) or board[r][c] != word[i] or (r, c) in path):
                return False
            
            # backtrack template: add(), dfs(i+1), remove()
            path.add((r, c))
            
            # 4 directions, move 1 step further
            res = (
                dfs(r-1, c, i+1) or
                dfs(r+1, c, i+1) or
                dfs(r, c-1, i+1) or
                dfs(r, c+1, i+1)
            )

            path.remove((r, c))

            return res

        for row in range(ROWS):
            for col in range(COLS):
                if dfs(row, col, 0): return True
        return False


'''

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        row = len(board)
        col = len(board[0])
        path = set()                     # current path 

        def dfs(r, c, i):
            if i == len(word):           # 成功找到
                return True
            if (r < 0 or c < 0 or r >= row or c >= col or 
                board[r][c] != word[i] or 
                (r, c) in path):
                return False             # 1.超出边界；2. 当前字符串不符合 word[i]；3. (r, c) 已经在当前路径中
                                         # 设立 path 的目的是不走回头路
            path.add((r, c))             # backtrack模板
            res = (dfs(r+1, c, i+1) or 
                   dfs(r-1, c, i+1) or 
                   dfs(r, c+1, i+1) or 
                   dfs(r, c-1, i+1))     # 四个方向都要探索 
            path.remove((r, c))          # 完成后要把当前字母坐标移出path
            return res
        
        for r in range(row):
            for c in range(col):
                if dfs(r, c, 0): return True     # board里每个字母都要遍历
        return False

# 因为这里主函数遍历整个board，所以在dfs里不需要主动去递归
# time: O(row * col * 4^len(word)) 
# board每个都要遍历，每个都要探索四个方向所有的情况

'''