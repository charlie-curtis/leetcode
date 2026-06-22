class Solution:
    def secondGreaterElement(self, nums: List[int]) -> List[int]:

        n = len(nums)
        #keep a sorted list
        #iterate from L to R

        #0,2, 4. Keep a tally, and the i-th index will try to satisfy indices to the left


        #insert value, idx, cnt
        stack = []
        first = []
        ans = [-1]*n
        for i in range(n):
            v = nums[i]
            while first and nums[i] > nums[first[-1]]:
                #anything in first has already found a match
                ans[first.pop()] = nums[i]
            
            t = []
            while stack and nums[i] > nums[stack[-1]]:
                t.append(stack.pop())
            first+=t[::-1]
            stack.append(i)
        return ans
