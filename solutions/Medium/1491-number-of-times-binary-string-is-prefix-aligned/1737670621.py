class Solution:
    def numTimesAllBlue(self, flips: List[int]) -> int:

        sl = SortedList()

        ans = 0
        for x in flips:
            sl.add(x)
            n = len(sl)
            high = sl[-1]
            if high == n:
                ans+=1
        return ans

        