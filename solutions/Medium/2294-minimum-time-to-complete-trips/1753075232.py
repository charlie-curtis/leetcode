class Solution:
    def minimumTime(self, time: List[int], T: int) -> int:


        n=len(time)

        def check(k):
            return sum([k//x for x in time]) >= T


        l=0
        r=10**15

        while l <= r:
            mid = l + (r-l)//2
            if check(mid):
                r=mid-1
            else:
                l= mid+1
        return l