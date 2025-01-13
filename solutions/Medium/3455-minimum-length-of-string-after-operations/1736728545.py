class Solution:
    def minimumLength(self, s: str) -> int:

        n = len(s)
        C = Counter(s)

        ans = 0
        for x in C.values():
            if x % 2:
                ans+=1
            else:
                ans+=2
        return ans