class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:

        n = len(nums)
        A = [0]*n

        for s,e in requests:
            A[s]+=1
            if e+1 < n:
                A[e+1]-=1

        pref = list(accumulate(A, initial = 0))
        MOD = 10**9+7
        pref.sort(reverse=True)
        nums.sort(reverse=True)

        ans = 0
        for a,b in zip(pref, nums):
            ans+=a*b
            ans%=MOD
        return ans
            
            
        