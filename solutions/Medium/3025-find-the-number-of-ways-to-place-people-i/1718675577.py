class Solution:
    def numberOfPairs(self, points: List[List[int]]) -> int:


        ans = 0
        for a,b in points:
            for c,d in points:
                if [a,b] == [c,d]:
                    continue
                if a <= c and b >= d:
                    ok = True
                    for e,f in points:
                        if [a,b] == [e,f] or [c,d] == [e,f]:
                            continue
                        if a <= e <= c and b >= f >= d:
                            ok = False
                            break
                    if ok:
                        ans+=1
        return ans


                #if i have points [1,3] and [3,1], I need a quick way to determine whether any point is in between.
                #the constraints are written in such a way that I can test each.