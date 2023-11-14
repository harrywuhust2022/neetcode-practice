class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        DIG = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        res = []
        def dfs(i, curStr):
            if len(curStr) == len(digits):           # "23" 只能 产生 "ab" 这样两位的string
                res.append(curStr)
                return
            
            for c in DIG[digits[i]]:                 # DIG[digits[i]] -> "2" : "abc"
                dfs(i+1, curStr + c)

        if digits:
            dfs(0, "")
        return res

'''

Example 1:
    Input: digits = "23"
    Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        DIG = { "2": "abc",                  # 看到题目第一反应先建立一个hash
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz" }

        def backtrack(i, curStr):
            if len(curStr) == len(digits):   # digits有可能输入3位，所以和长度相等
                res.append(curStr)
                return
            for c in DIG[digits[i]]:         # 难点：用for loop更新curStr, 并且递归
                backtrack(i+1, curStr + c)
        if digits:
            backtrack(0, "")
        return res

# Time: O(n* 4^n)

'''