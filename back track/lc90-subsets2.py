class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()                  # remember to sort nums, in order to gather all same elements.

        def dfs(i, subset):
            if i >= len(nums):
                res.append(subset.copy())
                return
            
            # Add nums[i]
            subset.append(nums[i])
            dfs(i+1, subset)
            subset.pop()

            # skip nums[i], but remember to skip all the same elements

            while i+1 < len(nums) and nums[i] == nums[i+1]:
                i += 1
            dfs(i+1, subset)
        
        dfs(i=0, subset=[])
        return res

'''

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()                         # 把重复的数字放在一起 

        def backtrack(i, subset):
            if i >= len(nums):
                res.append(subset.copy())   # update res 
                return
            
            # subset contains nums[i]
            subset.append(nums[i])
            backtrack(i + 1, subset)
            subset.pop()

            # subset does not contain nums[i]
            while i+1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1
            backtrack(i + 1, subset)
        backtrack(0, subset=[])
        return res

# idea: 这里做题的核心就是在处理重复数字的时候，用sort()把他们放在一起，然后 index 向后移动
# 但是仍然需要做一次 backtrack(i + 1)

'''