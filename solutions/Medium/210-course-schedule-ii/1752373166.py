class Solution:
    def findOrder(self, n: int, pre: List[List[int]]) -> List[int]:

        adj=defaultdict(set)
        C=Counter()
        for a,b in pre:
            if a not in adj[b]:
                adj[b].add(a)
                C[a]+=1
        q=[i for i in range(n) if C[i] ==0]
        
        ans=[]
        while q:
            i=q.pop()
            ans.append(i)
            for nxt in adj[i]:
                C[nxt]-=1
                if C[nxt]==0:
                    q.append(nxt)

        return ans if len(ans) == n else []
                