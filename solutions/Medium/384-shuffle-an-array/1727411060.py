class Solution:

    def __init__(self, nums: List[int]):
        self.original = nums
        

    def reset(self) -> List[int]:
        return self.original
        

    def shuffle(self) -> List[int]:

        out = []
        li = self.original.copy()
        while li:
            r = randint(0, len(li)-1)
            li[r],li[-1] = li[-1],li[r]
            out.append(li.pop())
        return out


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()