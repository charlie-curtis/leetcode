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

        d = {}
        #first pass through the graph, clone all the nodes and hash them
        def dfs(node):

            if node in d:
                return
            
            d[node] = Node(node.val)
            for u in node.neighbors:
                dfs(u)

        dfs(node)

        d2 = {}
        #second pass, setup the neighbors
        def dfs2(node):
            if node in d2:
                return
            d2[node] = True

            for u in node.neighbors:
                d[node].neighbors.append(d[u])
                dfs2(u)
        
        dfs2(node)
        return d[node]


