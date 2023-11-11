class Solution:
    def combinationSum2(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        nums.sort()

        def backtrack(i, subset, total):
            if total == target:
                res.append(subset.copy())
                return

            if i >= len(nums) or total > target:
                return

            # 1. Add nums[i]
            subset.append(nums[i])
            backtrack(i + 1, subset, total + nums[i])    # 这里是 i+1, 因为题目中说每个元素只能用一次
            subset.pop()

            # 2. skip nums[i]
            while i+1 < len(nums) and nums[i] == nums[i+1]:
                i += 1
            backtrack(i+1, subset, total)

        backtrack(i=0, subset=[], total=0)
        return res

'''

class Solution:
    def combinationSum2(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        nums.sort()                                         # 1. nums.sort， 把重复的元素放在一起

        def dfs(i, subset):
            if sum(subset) == target:
                res.append(subset.copy())
                return

            if i >= len(nums) or sum(subset) > target:      # 必须有这个返回条件，要不然会一直往下遍历叶子
                return

            subset.append(nums[i])
            dfs(i+1, subset)
            subset.pop()

            while i+1 < len(nums) and nums[i] == nums[i+1]: # 排除重复的元素结果
                i += 1
            dfs(i+1, subset)
        dfs(0, subset=[])
        return res

# 把此题拆解：lc90 (subset II) 和 如何求和返回

'''