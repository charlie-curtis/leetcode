class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        n = len(values)
        ans = -1
        prev = -1e15
        for x in values:
            ans = max(ans, x+prev)
            prev = max(x-1, prev-1)
            
        return ans