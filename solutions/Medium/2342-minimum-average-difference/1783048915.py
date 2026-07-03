class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:


        ssum1 = 0 
        ssum2 = sum(nums)
        best_idx = -1
        best = float('inf')
        n = len(nums)

        for i in range(n):
            ssum1+=nums[i]
            ssum2-=nums[i]

            a1 = ssum1//(i+1)
            a2 = ssum2//(n-1-i) if n-i-1 !=0 else 0
            d = abs(a1-a2)
            if d < best:
                best = d
                best_idx = i
        return best_idx

        