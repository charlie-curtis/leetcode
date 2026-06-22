class Solution:
    def minNumberOperations(self, target: List[int]) -> int:

        prev = 0
        ans = 0
        for x in target:
            if prev < x:
                #uphill climb
                ans+=(x-prev)
            prev = x
        return ans
                
                
        