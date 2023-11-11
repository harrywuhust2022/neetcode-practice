class solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
            res = []
            subset = []

            def dfs(i):
                if i >= len(nums):     # 返回结果条件： i >= len(nums),所以就可以有[]这样的
                    res.append(subset.copy())
                    return
                subset.append(nums[i]) # 第一种选择：把当前元素加入subset
                dfs(i + 1)
                subset.pop()           # 第二种选择：不把当前元素加入subset
                dfs(i + 1)
            dfs(0)
            return res

# backtracking, time: O(n * 2^n)
# 这道题res的变化情况就像一棵完全二叉树，新叶子每次有两个选择：加入当前元素 or 不加入当前元素