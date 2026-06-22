class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], left: List[int], right: List[int]) -> List[bool]:


        #500 queries, each of length 1000
        res = []
        for l,r in zip(left,right):

            A = sorted(nums[l:r+1])
            good = True
            n = len(A)
            for i in range(1,n-1):
                if A[i-1] - A[i] != A[i] - A[i+1]:
                    good = False
                    break
            res.append(good)
        return res
            
        