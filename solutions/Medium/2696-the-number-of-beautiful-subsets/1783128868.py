class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:

        ans, n = 0, len(nums)

        def bt(i, C):
            if i == n:
                nonlocal ans
                if len(C.keys()):
                    ans+=1
                return

            bt(i+1, C)
            if (C[nums[i] - k] == 0) and (C[nums[i] + k] == 0):
                C[nums[i]]+=1
                bt(i+1, C)
                C[nums[i]]-=1
        
        bt(0, Counter())
        return ans
        