from sortedcontainers import SortedList
class Solution:
    def subarraysWithMoreZerosThanOnes(self, nums: List[int]) -> int:

        MOD = 10**9 + 7

        balance = 0
        sl = SortedList()
        sl.add(0)
        ans = 0
        for x in nums:
            balance+=1 if x == 1 else -1
            idx = sl.bisect_left(balance)-1
            ans+=idx+1
            ans%=MOD
            sl.add(balance)
        return ans

