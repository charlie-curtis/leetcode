class Solution:
    def isGoodArray(self, nums: List[int]) -> bool:
        #editorial
        return reduce(lambda x,y: gcd(x,y), nums) == 1