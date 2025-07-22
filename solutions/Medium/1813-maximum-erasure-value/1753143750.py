class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        ans = ssum = j = 0
        n = len(nums)
        C = Counter()

        for i,x in enumerate(nums):
            ssum+=x
            C[x]+=1
            while len(C.keys()) < i-j+1:
                C[nums[j]]-=1
                ssum-=nums[j]
                if C[nums[j]] == 0:
                    del C[nums[j]]
                j+=1
            ans = max(ans, ssum)
        return ans