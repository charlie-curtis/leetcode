class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:

        n = len(nums)
        t = len(set(nums))
        C = Counter()

        i = j = 0
        ans = 0
        while i < n:
            while j < n and len(C.keys()) < t:
                C[nums[j]]+=1
                j+=1
            if len(C.keys()) == t:
                ans+=n-j+1
            else:
                break
            C[nums[i]]-=1
            if C[nums[i]] == 0:
                del C[nums[i]]
            i+=1
        return ans