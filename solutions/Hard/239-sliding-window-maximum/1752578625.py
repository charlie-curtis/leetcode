class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        d=deque()

        j=0
        out=[]

        for i,x in enumerate(nums):
            while d and i-d[0]+1 > k:
                d.popleft()
            while d and x >= nums[d[-1]]:
                d.pop()
            d.append(i)
            out.append(nums[d[0]])
            
        return out[k-1:]
        