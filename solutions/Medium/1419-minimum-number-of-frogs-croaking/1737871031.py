class Solution:
    def minNumberOfFrogs(self, s: str) -> int:

        C = Counter()
        cur = 0
        ans = 0
        for c in s:
            C[c]+=1
            prev = -1
            for x in 'croak'[::-1]:
                if C[x] < prev:
                    return -1
                prev = C[x]
                
            if c == 'c':
                cur+=1
            if c == 'k':
                cur-=1
            ans = max(ans, cur)

        seen = set(C.values())
        if len(seen) > 1:
            return -1
        return ans
        