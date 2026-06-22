class Solution:
    def longestSubarray(self, nums: List[int], k: int) -> int:

        n = len(nums)

        completed = 0
        C = Counter()
        j = ans = 0
        for i,x in enumerate(nums):
            if C[x] == 1:
                completed+=1
            C[x]+=1
            while completed > k:
                C[nums[j]]-=1
                if C[nums[j]] == 1:
                    completed-=1
                j+=1
            ans = max(ans, i-j+1)
        return ans