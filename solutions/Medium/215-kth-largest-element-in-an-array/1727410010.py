class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:


        #TTTTTTFFFFFFF

        l = min(nums) 
        r = max(nums)

        #checks if there are K numbers that are bigger/equalto than mid
        def check(mid):
            return len([x for x in nums if mid <= x]) >= k

        while l <= r:
            mid = l + (r-l)//2

            if check(mid):
                #there are >=k numbers bigger than mid, so increase mid
                l = mid + 1
            else:
                r = mid - 1


        return r
        