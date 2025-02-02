class Solution:
    def check(self, nums: List[int]) -> bool:

        n = len(nums)
        def check(k):
            prev = -1e15
            for i in range(n):
                if nums[(i+k)%n] < prev:
                    return False
                prev = nums[(i+k)%n]
            return True

        return any([check(x) for x in range(n)])

        