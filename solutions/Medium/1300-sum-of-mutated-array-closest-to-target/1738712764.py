class Solution:
    def findBestValue(self, A: List[int], target: int) -> int:

        n = len(A)
        A.sort()
        pref = list(accumulate(A, initial=0))

        best = 1e15
        v = -1
        for x in range(0, max(A)+1):
            idx = bisect_left(A, x) -1
            after = len(A) -idx -1
            if idx != -1:
                a = pref[idx+1] + after*x
            else:
                a = x*n
            if abs(a-target) < best:
                best =abs(a-target)
                v = x
            #print(x, a)
        return v

            