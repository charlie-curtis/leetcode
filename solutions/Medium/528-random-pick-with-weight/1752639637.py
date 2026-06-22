class Solution:

    def __init__(self, w: List[int]):
        self.pre = list(accumulate(w))
        

    def pickIndex(self) -> int:
        x = random.randint(1, self.pre[-1])
        return bisect_left(self.pre, x)
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()