class Solution:
    def findSmallestRegion(self, regions: List[List[str]], region1: str, region2: str) -> str:

        d = {}

        has_parent = set()
        for r in regions:
            first = r[0]
            rem = r[1:]
            for x in rem:
                has_parent.add(x)
            d[first] = rem

        ans = None
        def lca(me, p, q):
            nonlocal ans

            subs = d[me] if me in d else []

            cnt = 0
            for x in subs:
                if lca(x, p, q):
                    cnt+=1
            
            if me in [p,q]:
                cnt+=1
            if cnt == 2 and ans == None:
                ans = me
            return cnt
        
        #how find root? Only run the code for nodes that didnt have any parents
        for root in filter(lambda x: x not in has_parent, d.keys()):
            lca(root, region1, region2)
        return ans

        