class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        li = []
        for x in nums:
            idx = bisect_left(li, x)
            if idx == len(li):
                li.append(x)
            else:
                li[idx] = x
        return len(li)
        