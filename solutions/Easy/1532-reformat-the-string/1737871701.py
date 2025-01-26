class Solution:
    def reformat(self, s: str) -> str:
        digits = [x for x in s if not x.isalpha()]
        letters = [x for x in s if x.isalpha()]
        m,n = len(digits), len(letters)
        if abs(m-n) > 1:
            return ""

        out = []
        for i in range(min(m,n)):
            out.append(digits[i])
            out.append(letters[i])
        
        if m > n:
            out.append(digits[-1])
        elif m < n:
            out = [letters[-1]] + out
        return out