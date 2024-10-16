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
        if not node:
            return None
        visited = {}
        def dfs(curr_node: Node)->Node:
            if curr_node in visited:
                return visited[curr_node]
            clone = Node(curr_node.val)
            visited[curr_node] = clone
            for neighbor in curr_node.neighbors:
                clone.neighbors.append(dfs(neighbor))
            return clone

        return dfs(node)

# init visited to store cloned nodes
# dfs rec func
#   if current node is already cloned exists in the visited map, return its clone
#   otherwise create and add a new node to visited
#   for neighbor in the current node, clone its neighbors and add them to the clone' n list
# return the clone

# [[2, 4], [1,3], [2, 4], [1, 3]]
# node = 1, neighbors = 2, 4
# node = 2, neighbors = 1, 3. reuse 1 clone
# node = 3, neighbors = 2, 4 resue 2 clone
# node = 4, neighbors = 1, 3 1 and 3 reuse clone

# time complexity O(n)
# space complexity O(n) 