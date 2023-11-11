# Neetcode Graph Section.

When solving these graph problems, I find there are basically 3 templates to solve it. But the methods are DFS or BFS.

* Method: **DFS (recursive)** & **BFS (deque or minHeap)**
* Steps: 
    * build an adj map (hash). adj[node] = [nei1, nei2, ..., neiN]
    * `visit = set()`. It helps to mark all visited nodes
    * DFS or BFS template.

### Template 1: Island Problems
These problems are usually given a 2d array. Asking us to find the number/max area.

This is one of the most classic graph problems. **Use DFS + directions [[1,0], [-1,0], [0,1], [0,-1]]** to traverse the nodes in the grid.