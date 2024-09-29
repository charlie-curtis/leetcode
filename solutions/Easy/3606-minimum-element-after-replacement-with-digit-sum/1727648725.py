class Solution:
    def minElement(self, nums: List[int]) -> int:


        
        def go(x):

            ans = 0
            while x:
                ans+=x%10
                x//=10
            return ans

        
        return min([go(x) for x in nums])
        