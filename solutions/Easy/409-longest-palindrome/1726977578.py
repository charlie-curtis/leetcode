class Solution:
    def longestPalindrome(self, s: str) -> int:
        C = Counter(s)

        ans = 0
        odds = 0
        for k,v in C.items():
            ans+= (v//2)*2
            odds+= v % 2
        return ans if odds == 0 else ans+1

        