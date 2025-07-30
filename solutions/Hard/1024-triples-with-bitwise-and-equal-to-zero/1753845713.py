class Solution:
    def countTriplets(self, nums: List[int]) -> int:

        #gimmicky problem. O(N^2*2^16) should not pass (that's 6*10^7)
        n = len(nums)
        d = {}
        for i in range(n):
            for j in range(n):
                a = nums[i]&nums[j]
                if a not in d:
                    d[a] = 0
                d[a]+=1

        ans = 0
        for i in range(n):
            for j in d:
                if nums[i] & j == 0:
                    ans+=d[j]
        return ans
