class Solution:
    def rotateString(self, s: str, goal: str) -> bool:

        n = len(s)
        for i in range(n):
            a = s[:i]
            b = s[i:]
            if b+a == goal:
                return True
        return False
        