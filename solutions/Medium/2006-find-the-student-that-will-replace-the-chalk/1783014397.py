class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:

        ssum = sum(chalk)
        k%= ssum
        for i,x in enumerate(chalk):
            if x > k:
                return i
            k-=x
        return 0
        