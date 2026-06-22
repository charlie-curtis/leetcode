class Solution:
    def maxPossibleScore(self, nums: List[int], d: int) -> int:

        n = len(nums)

        nums.sort()

        l = 0
        r = 10**15

        #true if an answer can be found
        def check(T):
            expected = nums[0] + T 
            for x in nums[1:]:
                if x + d < expected:
                    #even if we use the highest number in our range, we can't reach the next number
                    return False
                #get the smallest number
                chosen = max(expected, x)
                expected = chosen + T
            return True


        #TTTTFFFFF
        while l <= r:
            mid = l + (r-l)//2
            if check(mid):
                l = mid + 1
            else:
                r = mid - 1
        return r