class Solution:
    def numWaterBottles(self, n: int, cost: int) -> int:

        have = n
        ans = 0
        while have - cost >= 0:
            ans+=cost
            have-=cost
            have+=1

        return ans + have
            
            
        