class Solution:
    def lastNonEmptyString(self, s: str) -> str:

        C = Counter(s)
        f = max(C.values())
        ans = []
        seen = set()
        for x in s[::-1]:
            if C[x] == f and x not in seen:
                seen.add(x)
                ans.append(x)

        return ''.join(ans[::-1])
        