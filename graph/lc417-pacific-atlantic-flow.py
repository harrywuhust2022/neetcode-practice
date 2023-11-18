class Solution:
    def pacificAtlantic(self, nums: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(nums), len(nums[0])
        atl, pac = set(), set()

        def dfs(r, c, visit, prevHeight):
            if r not in range(ROWS) or c not in range(COLS) or (r, c) in visit or nums[r][c] < prevHeight:
                return

            visit.add((r, c))
            dfs(r-1, c, visit, nums[r][c])
            dfs(r+1, c, visit, nums[r][c])
            dfs(r, c-1, visit, nums[r][c])
            dfs(r, c+1, visit, nums[r][c])
        
        for c in range(COLS):
            dfs(0, c, pac, nums[0][c])               # first row 肯定能到 pac，dfs看还有哪些cell能到 pac
            dfs(ROWS-1, c, atl, nums[ROWS-1][c])     # last row -> atl

        for r in range(ROWS):
            dfs(r, 0, pac, nums[r][0])               # first col -> pac
            dfs(r, COLS-1, atl, nums[r][COLS-1])     # last col  -> atl

        res = []
        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) in pac and (r, c) in atl:
                    res.append([r, c])
        return res

'''

class Solution:
    def pacificAtlantic(self, nums: List[List[int]]) -> List[List[int]]:
        rows, cols = len(nums), len(nums[0])
        pac, atl = set(), set()
        
        def dfs(r, c, visit, prevHeight):
            if (r in range(rows) and c in range(cols) and           # 一般来说条件都是四句话，然后在里面 dfs
                (r, c) not in visit and nums[r][c] >= prevHeight):  # 注意这里 nums[r][c] >= prevHeight, 看图，都是找数组中大的数字
                visit.add((r, c))
                dfs(r+1, c, visit, nums[r][c])
                dfs(r-1, c, visit, nums[r][c])
                dfs(r, c+1, visit, nums[r][c])
                dfs(r, c-1, visit, nums[r][c])
            else:
                return

        for c in range(cols):
            dfs(0, c, pac, nums[0][c])               # 统计从 nums 第一行 开始, 能到达 pacific 的数字坐标
            dfs(rows-1, c, atl, nums[rows-1][c])     # 统计从 nums 最后一行 开始, 能到达 atlantic 的数字坐标

        for r in range(rows):
            dfs(r, 0, pac, nums[r][0])               # 统计从 nums 第一列 开始, 能到达 pacific 的数字坐标
            dfs(r, cols-1, atl, nums[r][cols-1])     # 统计从 nums 最后一列 开始, 能到达 altantic 的数字坐标
        
        res = []
        for r in range(rows):
            for c in range(cols):
                if (r,c) in pac and (r,c) in atl:    # 如果这个数字 既在 pac 又在 atl 里，那就是答案坐标
                    res.append([r, c])
        return res

# nums 第一行 和 第一列 都是直接和 pacific 接触
# nums 最后一行 和 最后一列 都是直接和 Altantic 接触
# 所以在 dfs 的时候都是选用最接近的 set()

'''