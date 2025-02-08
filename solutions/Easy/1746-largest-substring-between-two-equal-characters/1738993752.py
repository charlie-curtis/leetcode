class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:

        ans = -1
        for i in range(26):
            c = chr(i + ord('a'))
            first, second = s.find(c), s.rfind(c)
            if first == -1:
                continue
            ans = max(ans, second-first-1)
        return ans
        