class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:

        #took me a minute - but you can find the answer by just alternating highs and lows
        #1,2,3,4,5,6 -> 1,6,2,5,3,4
        n = len(nums)
        if n == 1:
            return nums
        A = deque(sorted(nums))
        out = []
        for i in range(n):
            if i % 2 == 0:
                out.append(A.popleft())
            else:
                out.append(A.pop())
        return out