class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:

        n = len(nums)
        C = Counter()
        for i in range(n):
            for j in range(i+1, n):
                a,b = nums[i],nums[j]
                C[a*b]+=1
        

        return sum([8*x*(x-1)//2 for x in C.values()])

        