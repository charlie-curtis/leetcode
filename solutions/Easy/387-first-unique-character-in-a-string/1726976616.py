class Solution:
    def firstUniqChar(self, s: str) -> int:
        C = Counter(s)
        for i in range(len(s)):
            if C[s[i]] == 1:
                return i
        return -1
        