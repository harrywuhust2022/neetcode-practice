import collections
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visit = set()
        island = 0

        def bfs(r, c):
            q = collections.deque()
            visit.add((r, c))
            q.append((r, c))

            directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]

            # BFS 不需要递归，直接while loop 迭代 q
            while q:
                row, col = q.popleft()
                for dr, dc in directions:
                    newR, newC = row + dr, col + dc
                    if (newR, newC) not in visit and newR in range(ROWS) and newC in range(COLS) and grid[newR][newC] == "1":
                        visit.add((newR, newC))
                        q.append((newR, newC))
        
        for row in range(ROWS):
            for col in range(COLS):
                if (row, col) not in visit and grid[row][col] == "1":
                    bfs(row, col)
                    island += 1
        return island


# *******************************************************
# DFS

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visit = set()
        island = 0

        # dfs这个函数只需要帮助更新 visit
        def dfs(r, c):
            if (r, c) in visit or r not in range(ROWS) or c not in range(COLS) or grid[r][c] != "1":
                return

            visit.add((r, c))
            dfs(r-1, c)
            dfs(r+1, c)
            dfs(r, c-1)
            dfs(r, c+1)

        for row in range(ROWS):
            for col in range(COLS):
                if (row, col) not in visit and grid[row][col] == "1":
                    dfs(row, col)
                    island += 1
        return island

# Time: O(n*m)

'''
Example 1:

Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1

BFS

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid: return 0
        
        rows, cols = len(grid), len(grid[0])
        island = 0
        visit = set()

        def bfs(r, c):                                       # bfs目的在于更新visit
            q = collections.deque()
            visit.add((r, c))
            q.append((r, c))
            
            while q:
                row, col = q.popleft()
                direction = [[1,0], [-1,0], [0,1], [0,-1]]    # 可以学习一下怎么写四个方向
                for dr, dc in direction:
                    r, c = row + dr, col + dc
                    if ((r, c) not in visit and 
                        r in range(rows) and
                        c in range(cols) and
                        grid[r][c] == "1"):
                        q.append((r, c))
                        visit.add((r, c))

        for r in range(rows):
            for c in range(cols):
                if (r, c) not in visit and grid[r][c] == "1":
                    bfs(r, c)
                    island += 1
        return island

# idea: 这道题框架：暴力搜索每个点，如果没访问过 && grid[r][c] == 1，那就对这个点进行bfs搜索
# 也可以dfs搜索，目的在于把连接的整片岛屿都划出来，后续不再访问这片区域

'''