class Solution:
    def isConsecutive(self, nums: List[int]) -> bool:

        mmin = min(nums)
        n = len(nums)

        i = 0
        while i < n:
            v = nums[i]
            expected_idx = v-mmin
            if i == expected_idx:
                #this element is in order, continue
                i+=1
                continue

            #if the value is out of bounds or there is a duplicate
            if expected_idx < 0 or expected_idx >= n or nums[expected_idx] == v:
                return False

            nums[i], nums[expected_idx] = nums[expected_idx], nums[i]
        return True
            