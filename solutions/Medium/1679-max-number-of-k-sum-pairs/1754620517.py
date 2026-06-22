class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:

        C = Counter()
        ans = 0
        for x in nums:
            t = k-x
            if C[t] > 0:
                ans+=1
                C[t]-=1
            else:
                C[x]+=1
        return ans
        