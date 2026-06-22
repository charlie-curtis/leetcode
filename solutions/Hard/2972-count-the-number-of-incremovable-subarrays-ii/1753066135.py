class Solution:
    def incremovableSubarrayCount(self, nums: List[int]) -> int:
        #you want to find the suffix closest to you that is "good"

        n = len(nums)
        indices = [n-1]
        for i in range(n-2,-1,-1):
            if nums[i] < nums[i+1]:
                indices.append(i)
            else:
                break
        

        ans = 0
        good = True
        j = n-1
        for i in range(n):
            if not good:
                break
            if i > 0 and nums[i-1] >= nums[i]:
                #delay breaking the loop until next iteration - this is because we're removing this element this iteration, so it won't count as an out-of-order prefix
                good = False
            while indices and (indices[-1] <= i or (i > 0 and nums[indices[-1]] <= nums[i-1])):
                indices.pop()
            if not indices:
                #have to remove everything starting from this idx
                ans+=1
            else:
                #this means that some suffix is in order, so we have the option
                #of either deleting it or keeping it
                #3,6,[7],3,2,5,7
                #if we are processing the 7, we know we atleast need to delete [7,3], but we could also delete [7,3,2] or [7,3,2,5] or [7,3,2,5,7]
                ans+=n -indices[-1]+1
        return ans