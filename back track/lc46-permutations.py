class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        def dfs(perm, used, res):
            if len(perm) == len(nums):
                res.append(perm.copy())
                return

            for i, num in enumerate(nums):
                if used[i] == True:
                    continue

                perm.append(num)
                used[i] = True
                dfs(perm, used, res)
                perm.pop()
                used[i] = False
        res = []
        dfs(perm=[], used=[False]*len(nums), res=res)
        return res

'''

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def dfs(perm, used, res):
            
            if len(perm) == len(nums):       # 判断终点条件：update res & return
                res.append(perm.copy())
                return
            
            for i, num in enumerate(nums):   # 遍历整个 nums 数组
                if used[i]:
                    continue                 # 如果这个数字已经用过了，直接往后走
                
                perm.append(num)             # 加入新的数字，并把 used[i] 更新
                used[i] = True
                
                dfs(perm, used, res)         # 继续往下遍历（本质 == dfs(i+1)）
                
                perm.pop()                   # 模板：加入一个之后，要记得pop()
                used[i] = False              # update used[i]
        res = []
        dfs(perm=[], used=[False]*len(nums), res=res)
        return res

'''