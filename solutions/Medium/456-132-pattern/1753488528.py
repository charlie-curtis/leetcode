class Solution:
    def find132pattern(self, nums: List[int]) -> bool:


        mn = 10**9
        n = len(nums)
        mins = [mn]*n
        for i in range(n):
            mins[i] = mn
            mn = min(mn, nums[i])
        
        d = deque()
        for i in range(n-1, -1,-1):
            mn = mins[i]
            while d and d[0] < nums[i]:
                if mn < d.popleft() < nums[i]:
                    return True
            d.appendleft(nums[i])
        return False
        