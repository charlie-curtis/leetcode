class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:

        indegree = Counter()
        for u,v in edges:
            indegree[v]+=1
            indegree[u]+=0



        return [k for k,v in indegree.items() if v == 0]
        