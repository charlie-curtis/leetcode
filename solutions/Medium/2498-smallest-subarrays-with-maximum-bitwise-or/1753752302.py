class Solution:
    def smallestSubarrays(self, nums: List[int]) -> List[int]:
        n=len(nums)
        out=[n-1]*n
        j = n-1
        C=Counter()
        def good():
            for i in range(32):
                if (1<<i) & mx:
                    if C[i] <= 0:
                        return False
            return True
        def add(x):
            for i in range(32):
                C[i]+=1 if ((x&(1<<i)) > 0) else 0
        def sub(x):
            for i in range(32):
                C[i]-=1 if ((x&(1<<i)) > 0) else 0
        mx = 0
        for i in range(n-1,-1,-1):
            mx|=nums[i]
            add(nums[i])
            while j >=i and good():
                sub(nums[j])
                j-=1
            out[i] = j-i+2
        return out
            