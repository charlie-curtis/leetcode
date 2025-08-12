"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:

        #get rid of the id concept and just use the 0-based indexing
        mmap = {}
        n = len(employees)
        vals = [0]*n
        adj = [[] for _ in range(n)]
        for i,nei in enumerate(employees):
            mmap[nei.id] = i
            vals[i] = nei.importance
        for i,nei in enumerate(employees):
            adj[i] = [mmap[x] for x in nei.subordinates]
        
        def dfs(i):
            ans = vals[i]
            for nxt in adj[i]:
                ans+=dfs(nxt)
            return ans

        return dfs(mmap[id])

        
        