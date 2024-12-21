class Solution:
    def checkValidCuts(self, n: int, rectangles: List[List[int]]) -> bool:


        def check(intervals):
            intervals.sort(key= lambda r: (r[0], -r[1]))

            f = []
            for start,end in intervals:
                if not f or f[-1][1] <= start:
                    f.append([start,end])
                else:
                    f[-1][1] = max(f[-1][1], end)

            return len(f) >= 3





        a = [(r[0], r[2]) for r in rectangles]
        b = [(r[1], r[3]) for r in rectangles]
        return check(a) or check(b)
        
        