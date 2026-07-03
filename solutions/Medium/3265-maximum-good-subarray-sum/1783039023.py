class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:

        ssum = 0
        n = len(nums)
        H = {}
        NEGINF = float('-inf')
        ans = NEGINF
        for i,x in enumerate(nums):
            ssum+=x
            check = [x-k, x+k]
            for j in check:
                if j in H:
                    ans = max(ssum-H[j] + j, ans)

            if x not in H or H[x] > ssum:
                H[x] = ssum
        
        if ans == NEGINF:
            return 0
        return ans


