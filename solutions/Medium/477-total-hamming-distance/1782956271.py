class Solution:
    def totalHammingDistance(self, nums: List[int]) -> int:

        n = len(nums)
        ones = Counter()
        zeros = Counter()
        ans = 0
        for i in range(n):
            for j in range(32):
                
                if nums[i]&(1<<j):
                    #this bit is set, so if we previously saw zeros at this pos, that is a hamming weight diff
                    ans+=zeros[j]
                    ones[j]+=1
                else:
                    ans+=ones[j]
                    zeros[j]+=1
        return ans