class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:

        li = []
        for x in nums:
            idx = bisect_left(li, x)
            if idx == len(li):
                li.append(x)
            else:
                li[idx] = x
        return len(li) >= 3
        