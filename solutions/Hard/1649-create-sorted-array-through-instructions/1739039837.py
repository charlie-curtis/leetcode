class Solution:
    def createSortedArray(self, instructions: List[int]) -> int:


        sl = SortedList()

        ans = 0
        MOD = 10**9 + 7
        for x in instructions:
            a = sl.bisect_left(x)
            b = len(sl) - sl.bisect_right(x)
            ans+=min(a,b)
            ans%=MOD

            sl.add(x)
        return ans
        