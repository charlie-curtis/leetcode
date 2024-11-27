class Solution:
    def removeOnes(self, grid: List[List[int]]) -> bool:

        seen = set()

        for li in grid:
            seen.add(''.join([str(x) for x in li]))


        if len(seen) > 2:
            return False

        if len(seen) == 1:
            return True

        a,b = list(seen)

        for i in range(len(a)):
            if int(a[i]) + int(b[i]) != 1:
                return False
        return True
        