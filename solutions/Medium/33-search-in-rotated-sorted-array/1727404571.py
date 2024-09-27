class Solution:
    def search(self, nums: List[int], target: int) -> int:


        def bs(l, r):

            while l <= r:
                mid = l + (r-l)//2

                if nums[mid] == target:
                    return mid
                
                if nums[mid] > target:
                    r = mid - 1
                else:
                    l = mid + 1

            return -1


        if nums[0] < nums[-1]:
            return bs(0, len(nums)-1)

        l,r  = 0, len(nums)-1

        while l <= r:

            mid = l + (r-l)//2
            if nums[mid] <= nums[-1]:
                r = mid -1
            else:
                l = mid + 1

        p = l
        return max([bs(0, p-1), bs(p, len(nums)-1)])
