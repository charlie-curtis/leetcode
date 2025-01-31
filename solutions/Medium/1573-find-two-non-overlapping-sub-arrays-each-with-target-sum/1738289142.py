class Solution:
    def minSumOfLengths(self, A: List[int], target: int) -> int:


        d = {}
        d[0] = -1

        ssum = 0
        seen = []
        for i,x in enumerate(A):
            ssum+=x
            if ssum - target in d:
                seen.append([d[ssum-target], i])
            d[ssum] = i


        seen.sort(key=lambda x: x[1])

        sl = SortedDict()
        ans = 1e15
        for s,e in seen:
            idx = sl.bisect_right(s) - 1
            if idx != -1:
                ans = min(ans, sl.peekitem(idx)[1] + (e-s))
            if not sl or sl.peekitem(-1)[1] > e-s:
                sl[e] = e-s
        return ans if ans != 1e15 else -1
            
            
        
            
        