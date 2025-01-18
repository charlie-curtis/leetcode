class Solution:
    def isPalindrome(self, x: int) -> bool:

        if x < 0:
            return False

        out = 0
        original = x
        while x:
            out = out*10 + (x % 10)
            x//=10
        print(out, original)
        return out == original
        