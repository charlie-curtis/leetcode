class Solution:
    def evenProduct(self, nums: List[int]) -> int:

        #odd product = contains only odd numbers
        odds = 0
        total = 0
        n = len(nums)
        for x in nums:
            if x % 2 == 1:
                odds+=1
            else:
                odds = 0
            total+=odds

        return n*(n+1)//2 - total


        