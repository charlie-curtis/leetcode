class Solution:
    def maximizeSweetness(self, sweetness: List[int], k: int) -> int:

        l = 1
        r = sum(sweetness)

        n = len(sweetness)
        def check(mid):
            rem = k
            ssum = 0
            for i in range(n):
                if ssum >= mid:
                    ssum = sweetness[i]
                    rem-=1
                else:
                    ssum+=sweetness[i]

            return (rem == 0 and ssum >= mid) or rem < 0


        while l <= r:

            mid = l + (r-l)//2
            if check(mid):
                l = mid + 1
            else:
                r = mid -1

        return r
        