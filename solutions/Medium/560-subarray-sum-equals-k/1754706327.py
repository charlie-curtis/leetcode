class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        C = Counter()
        C[0]+=1
        ans = 0
        ssum = 0
        for x in nums:
            ssum+=x
            ans+=C[ssum-k]
            C[ssum]+=1
        return ans
        