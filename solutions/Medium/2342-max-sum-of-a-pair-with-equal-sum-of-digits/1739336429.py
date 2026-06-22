class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        A=[[sum([int(x) for x in str(n)]), n] for n in nums]
        d,ans={},-1
        for h,n in A:
            if h in d:
                ans=max(ans,d[h]+n)
                d[h]=max(d[h],n)
                
            else:d[h]=n
        return ans