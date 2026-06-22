class Solution:
    def countGood(self, nums: List[int], k: int) -> int:

        n = len(nums)
        C = Counter()
        ssum = ans = j = 0
        for i,x in enumerate(nums):
            ssum+=C[x]
            C[x]+=1
            while ssum >= k:
                ans+=(n-i)
                C[nums[j]]-=1
                ssum-=C[nums[j]]
                j+=1
        return ans



        