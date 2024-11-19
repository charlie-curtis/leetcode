class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:


        j = 0
        n = len(nums)
        ans = 0
        ssum = 0
        C = Counter()
        for i in range(n):
            ssum+=nums[i]
            C[nums[i]]+=1

            if i-j+1 > k:
                C[nums[j]]-=1
                if C[nums[j]] == 0:
                    del C[nums[j]]
                ssum-=nums[j]
                j+=1

            if len(C.keys()) == k:
                ans = max(ans, ssum)
        return ans
        