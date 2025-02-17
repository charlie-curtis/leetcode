class Solution:
    def maxStudentsOnBench(self, studs: List[List[int]]) -> int:
        d=defaultdict(set)
        ans=0
        for s,b in studs:
            d[b].add(s)
            ans=max(ans, len(d[b]))
        return ans
            