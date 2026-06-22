class Solution:
    def largestNumber(self, cost: List[int], target: int) -> str:

        @cache
        def dp(rem):
            if rem == 0:
                return ""

            best = -1 
            winner = ""
            for j in range(9, 0, -1):
                c = cost[j-1]
                if c <= rem:
                    res = dp(rem-c)
                    if res != -1 and (best == -1 or len(res) > best):
                        best = len(res)
                        winner = str(j) + res
            if best == -1:
                return -1
            else:
                return winner

        res = dp(target)
        return res if res != -1 else "0"