class Solution:
    def isPalindrome(self, s: str) -> bool:

        s = s.lower()
        s = ''.join([x for x in s if x.isalnum()])
        return s[::-1] == s

        