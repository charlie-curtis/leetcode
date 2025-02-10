class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        C= Counter()
        n=len(wall)
        for li in wall:
            if len(li)>1:
                C+=Counter(list(accumulate(li[:-1])))
        li = C.values()
        if not li: return n
        return n - max(li)
        