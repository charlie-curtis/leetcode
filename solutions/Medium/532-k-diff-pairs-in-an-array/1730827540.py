class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:

        ans = set() 
        seen = set()
        for x in nums:
            if x-k in seen:
                ans.add((x-k, x))
            if x+k in seen:
                ans.add((x, x+k))
            seen.add(x)

        return len(ans)

        