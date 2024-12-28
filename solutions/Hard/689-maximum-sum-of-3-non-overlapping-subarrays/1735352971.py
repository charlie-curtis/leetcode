class Solution:
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        
        n = len(nums)
        cans = [-1]*n
        
        j = ssum = 0
        for i in range(n):
            ssum+=nums[i]
            if i - j + 1 > k:
                ssum-=nums[j]
                j+=1
                
            if i - j + 1 == k:
                cans[j] = ssum
                
                
        bl = [-1]*n
        lin = [-1]*n
        br = [-1]*n
        rin = [-1]*n
        
        b = j = -1
        for i in range(n):
            if cans[i] > b:
                b = cans[i]
                j = i
            bl[i] = b
            lin[i] = j
            
        b = j = -1
        for i in range(n-1, -1, -1):
            if cans[i] >= b:
                b = cans[i]
                j = i
            br[i] = b
            rin[i] = j
            
        b = -1
        ans = []
        for i in range(k, n-k):
            c = cans[i] + bl[i-k] + br[i+k]
            if c > b:
                b = c
                ans = [lin[i-k], i, rin[i+k]]

        return ans
                
            