class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:

        adj = {}
        indegree = Counter()
        for i in range(n):
            l = leftChild[i]
            r = rightChild[i]
            if r != -1:
                indegree[i]+=1
                if r in adj:
                    return False
                adj[r] = i
            if l != -1:
                indegree[i]+=1
                if l in adj:
                    return False
                adj[l] = i

        if sum(indegree.values()) +1 < n:
            return False


        seen = set()
        q = []
        for i in range(n):
            if indegree[i] == 0:
                q.append(i)

        while q:
            idx = q.pop()
            seen.add(idx)
            if idx in adj:
                nxt = adj[idx]
                indegree[nxt]-=1
                if indegree[nxt] == 0:
                    q.append(nxt)

        return sum(indegree.values()) == 0
