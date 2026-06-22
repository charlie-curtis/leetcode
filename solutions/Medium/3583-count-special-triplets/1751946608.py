class Solution:
    def specialTriplets(self, nums: List[int]) -> int:

        n = len(nums)
        C = Counter()
        left = [0]*n
        right = [0]*n
        for i,x in enumerate(nums):
            left[i] = C[2*x]
            C[x]+=1
        
        C = Counter()
        for i in range(n-1, -1, -1):
            x = nums[i]
            right[i] = C[2*x]
            C[x]+=1

        MOD = 10**9 + 7
        ans = 0
        for i in range(n):
            ans+=right[i]*left[i]
            ans%=MOD
        return ans