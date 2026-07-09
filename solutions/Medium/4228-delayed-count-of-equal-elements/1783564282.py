class Solution:
    def delayedCount(self, nums: List[int], k: int) -> List[int]:


        n = len(nums)
        d = defaultdict(deque)
        out = [0]*n
        for i in range(n-1, -1, -1):
            x = nums[i]
            li = d[x]
            out[i] = len(li) - bisect_right(li, i+k)
            d[x].appendleft(i)
        return out

        