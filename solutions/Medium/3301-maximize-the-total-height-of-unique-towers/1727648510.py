class Solution:
    def maximumTotalSum(self, heights: List[int]) -> int:


        heights.sort(reverse=True)

        ans = 0
        allowed = 1e10
        for x in heights:
            allowed = min(x, allowed)
            if allowed <= 0:
                return -1
            ans+=allowed
            allowed-=1
        return ans


        