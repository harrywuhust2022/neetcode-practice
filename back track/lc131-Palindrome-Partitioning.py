class Solution:
    def isP(self, s, l, r):
        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True

    def partition(self, s: str) -> List[List[str]]:
        res = []
        parti = []

        def dfs(i):
            if i >= len(s):
                res.append(parti.copy())
                return

            for j in range(i, len(s)):
                if self.isP(s, i, j):
                    parti.append(s[i:j+1])
                    dfs(j+1)
                    parti.pop()

        dfs(0)
        return res

'''
Given a string s, partition s such that every substring of the partition is a palindrome. 
Return all possible palindrome partitioning of s.

Example 1:
    Input: s = "aab"
    Output: [["a","a","b"],["aa","b"]]

Example 2:
    Input: s = "a"
    Output: [["a"]]


class Solution:
    def isP(self, s, l, r):
        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1                           # 别忘记更新 l, r 
        return True

    def partition(self, s: str) -> List[List[str]]:
        res = []
        parti = []

        def dfs(i):
            if i >= len(s):
                res.append(parti.copy())
                return
            
            for j in range(i, len(s)):       # backtrack 模板
                if self.isP(s, i, j):
                    parti.append(s[i:j+1])
                    dfs(j + 1)
                    parti.pop()
        dfs(0)
        return res

# 思路：写一个子函数：self.isP用于判断是否是回文串
# 对于 s , 采用 backtracking 思路，如果partition 是回文串，继续dfs


    
'''