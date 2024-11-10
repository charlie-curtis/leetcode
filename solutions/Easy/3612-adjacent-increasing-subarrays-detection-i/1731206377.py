class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        print("STARTING")
        n = len(nums)
        def is_good(i):
            
            if i + k > n:
                return False
            for j in range(i+1,i+k):
                if nums[j] <= nums[j-1]:
                    return False
            return True
        
        
        
        for i in range(n):
            #print(is_good(i), is_good(i+k), i, i+k)
            if is_good(i) and is_good(i+k):
                return True
        return False
            
        