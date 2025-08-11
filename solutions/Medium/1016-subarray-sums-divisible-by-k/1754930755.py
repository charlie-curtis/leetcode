class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:

        C = Counter()
        C[0]+=1

        ssum = 0
        ans = 0
        for x in nums:
            ssum+=x
            ans+=C[ssum%k]
            C[ssum%k]+=1
        return ans

        