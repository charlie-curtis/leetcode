class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:

        ans = 0
        C = Counter()
        C[0] = 1
        odds = 0
        for x in nums:
            if x%2:
                odds+=1
            ans+=C[odds-k]
            C[odds]+=1
        return ans
        