class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:

        T = sum(nums)
        if T % k: return False
        target = T // k
        n = len(nums)
        @cache
        def dp(used, cur, j):
            if j == k:
                return True
            if used == 2**(n) -1:
                return False

            for i in range(n):
                if (1<<i)&used == 0:
                    #not used
                    if cur + nums[i] == target:
                        if dp(used|(1<<i), 0, j+1):
                            return True
                    elif cur + nums[i] < target and dp(used|(1<<i), cur + nums[i], j):
                        return True
            return False
        return dp(0, 0, 0)