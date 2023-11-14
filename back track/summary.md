# Summary of backtrack
这类问题主要是集中在 排列组合问题上:
* 1. subset; 
* 2. combination sum; 
* 3. permutation
* 4. 字符串的partition
* 5. 有时候也会结合 dfs 4 个方向的递归搜索 (二维数组)

解题思路：
1. 先确定是backtrack思路；
2. 写主要部分，如何调用 `def dfs()`, dfs应该return什么结果 / 或者不返回结果，只需要更新 `res = []`.
3. 开始写 `def dfs(row, col, i)`, 先确定传进来的参数是什么：
* 3.1. `if condition1: return True / or update res`
* 3.2. `if condition2: return False` (判断边界条件是否超过)
* 3.3. backtrack template:
```
add(nums[i])
dfs(i+1)
remove(nums[i])
```
* 3.4. `return res` 
