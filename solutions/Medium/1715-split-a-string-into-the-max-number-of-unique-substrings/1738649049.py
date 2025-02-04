class Solution:
    def maxUniqueSplit(self, s: str) -> int:

        seen = set()
        n = len(s)

        def bt(i):

            if i == n:
                return 0

            #j is the endpoint
            ans = 0
            for j in range(i,n):
                can = s[i:j+1]
                if can not in seen:
                    seen.add(can)
                    ans = max(ans, 1 + bt(j+1))
                    seen.remove(can)
            return ans
        return bt(0)
        