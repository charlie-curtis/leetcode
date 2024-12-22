class Solution:
    def maxDistinctElements(self, nums: List[int], k: int) -> int:
        nums.sort()

        next_available = -1e15
        ans = 0
        for x in nums:
            if x > next_available:
                chosen = max(next_available, x-k)
                ans+=1
            elif x == next_available:
                chosen = x
                ans+=1
            elif x + k >= next_available:
                chosen = next_available
                ans+=1
            else:
                continue

            next_available = chosen+1
        return ans
                
                
            
            
        