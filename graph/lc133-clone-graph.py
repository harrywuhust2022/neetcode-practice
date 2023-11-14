"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        old2new = {}

        def dfs(node):
            if node in old2new:
                return old2new[node]

            copy = Node(node.val)
            old2new[node] = copy

            for nei in node.neighbors:
                copy.neighbours.append(dfs(nei))
            
            return copy
        
        return dfs(node) if node else None

'''

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        OldToNew = {}
        def dfs(node):
            if node in OldToNew:
                return OldToNew[node]
            
            copy = Node(node.val)               # 先对当前这个node拷贝：建立一个新的node
            OldToNew[node] = copy               # 把它加入 old2new 哈希映射

            for nei in node.neighbors:          # 遍历neighbors
                copy.neighbors.append(dfs(nei)) # 递归连接 neighbors
            return copy
        return dfs(node) if node else None

'''